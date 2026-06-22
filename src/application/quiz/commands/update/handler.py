from src.application.shared.interfaces import ICommandHandler
from src.application.quiz.commands.base_handler import BaseQuizCommandHandler
from src.application.quiz.commands.update.command import UpdateQuizCommand


class UpdateQuizCommandHandler(BaseQuizCommandHandler, ICommandHandler[UpdateQuizCommand, None]):
    async def handle(self, command: UpdateQuizCommand) -> None:
        async with self._uow:
            quiz = await self._get_quiz(command.quiz_id)

            if command.respondent_id is not None:
                quiz.change_respondent(new_respondent_id=command.respondent_id)

            if command.title is not None:
                quiz.rename(new_title=command.title)

            await self._save_quiz(quiz)
