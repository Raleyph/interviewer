from src.application.shared.interfaces import ICommandHandler
from src.application.quiz.commands.base_handler import BaseQuizCommandHandler
from src.application.quiz.commands.rollback.command import RollbackQuizCommand


class RollbackQuizCommandHandler(BaseQuizCommandHandler, ICommandHandler[RollbackQuizCommand, None]):
    async def handle(self, command: RollbackQuizCommand) -> None:
        async with self._uow:
            quiz = await self._get_quiz(command.quiz_id)
            quiz.rollback()
            await self._save_quiz(quiz)
