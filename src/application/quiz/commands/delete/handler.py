from src.application.shared.interfaces import ICommandHandler
from src.application.quiz.commands.base_handler import BaseQuizCommandHandler
from src.application.quiz.commands.delete.command import DeleteQuizCommand


class DeleteQuizCommandHandler(BaseQuizCommandHandler, ICommandHandler[DeleteQuizCommand, None]):
    async def handle(self, command: DeleteQuizCommand) -> None:
        async with self._uow:
            quiz = await self._get_quiz(command.quiz_id)
            await self._uow.context.quizzes.delete(quiz)
