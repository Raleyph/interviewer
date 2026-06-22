from src.application.shared.interfaces import ICommandHandler
from src.application.quiz.commands.base_handler import BaseQuizCommandHandler
from src.application.quiz.commands.remove_question.command import RemoveQuizQuestionCommand


class RemoveQuizQuestionCommandHandler(BaseQuizCommandHandler, ICommandHandler[RemoveQuizQuestionCommand, None]):
    async def handle(self, command: RemoveQuizQuestionCommand) -> None:
        async with self._uow:
            quiz = await self._get_quiz(command.quiz_id)
            quiz.remove_question(question_id=command.question_id)
            await self._save_quiz(quiz)
