from src.application.shared.interfaces import ICommandHandler
from src.application.quiz.commands.base_handler import BaseQuizCommandHandler
from src.application.quiz.commands.rename.command import RenameQuizCommand


class RenameQuizCommandHandler(BaseQuizCommandHandler, ICommandHandler[RenameQuizCommand, None]):
    async def handle(self, command: RenameQuizCommand) -> None:
        quiz = await self._get_quiz(command.quiz_id)
        quiz.rename(new_title=command.new_title)
        await self._save_quiz(quiz)
