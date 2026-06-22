from src.application.shared.interfaces import ICommandHandler
from src.application.quiz.commands.base_handler import BaseQuizCommandHandler
from src.application.quiz.commands.change_respondent.command import ChangeQuizRespondentCommand


class ChangeQuizRespondentCommandHandler(BaseQuizCommandHandler, ICommandHandler[ChangeQuizRespondentCommand, None]):
    async def handle(self, command: ChangeQuizRespondentCommand) -> None:
        quiz = await self._get_quiz(command.quiz_id)
        quiz.change_respondent(new_respondent_id=command.new_respondent_id)
        await self._save_quiz(quiz)
