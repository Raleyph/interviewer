from uuid import UUID

from src.domain.quiz import Quiz

from src.application.shared.interfaces import ICommandHandler, IUnitOfWork
from src.application.quiz.commands.create.command import CreateQuizCommand
from src.application.user.read_repository import IUserReadRepository


class CreateQuizCommandHandler(ICommandHandler[CreateQuizCommand, UUID]):
    def __init__(
            self,
            uow: IUnitOfWork,
            user_read_repository: IUserReadRepository
    ):
        self._uow = uow
        self._user_read_repository = user_read_repository

    async def handle(self, command: CreateQuizCommand) -> UUID:
        async with self._uow:
            respondent = await self._user_read_repository.get_by_username(command.respondent_username)

            if respondent is None:
                raise

            quiz = Quiz.create(
                interviewer_id=command.interviewer_id,
                respondent_id=respondent.id,
                title=command.title
            )

            await self._uow.context.quizzes.add(quiz)

            return quiz.id
