from uuid import UUID

from src.application.shared.interfaces import ICommandHandler
from src.application.quiz.commands.base_handler import BaseQuizCommandHandler
from src.application.quiz.commands.add_question.command import AddQuizQuestionCommand


class AddQuizQuestionCommandHandler(BaseQuizCommandHandler, ICommandHandler[AddQuizQuestionCommand, UUID]):
    async def handle(self, command: AddQuizQuestionCommand) -> UUID:
        async with self._uow:
            quiz = await self._get_quiz(command.quiz_id)
            question_id = quiz.add_question(text=command.text, notice=command.notice)
            await self._save_quiz(quiz)

            return question_id
