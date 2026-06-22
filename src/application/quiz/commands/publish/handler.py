from src.application.quiz.commands.base_handler import BaseQuizCommandHandler
from src.application.quiz.commands.publish.command import PublishQuizCommand
from src.application.shared.interfaces import ICommandHandler


class PublishQuizCommandHandler(BaseQuizCommandHandler, ICommandHandler[PublishQuizCommand, None]):
    async def handle(self, command: PublishQuizCommand) -> None:
        async with self._uow:
            quiz = await self._get_quiz(command.quiz_id)
            quiz.publish()
            await self._save_quiz(quiz)
