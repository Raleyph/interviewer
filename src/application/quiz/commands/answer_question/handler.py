from src.application.shared.interfaces import ICommandHandler
from src.application.quiz.commands.base_handler import BaseQuizCommandHandler
from src.application.quiz.commands.answer_question.command import AnswerQuizQuestionCommand


class AnswerQuizQuestionCommandHandler(BaseQuizCommandHandler, ICommandHandler[AnswerQuizQuestionCommand, None]):
    async def handle(self, command: AnswerQuizQuestionCommand) -> None:
        quiz = await self._get_quiz(command.quiz_id)
        quiz.answer_question(question_id=command.question_id)
        await self._save_quiz(quiz)
