from src.application.shared.interfaces import ICommandHandler
from src.application.quiz.commands.base_handler import BaseQuizCommandHandler
from src.application.quiz.commands.edit_question.command import EditQuizQuestionCommand


class EditQuizQuestionCommandHandler(BaseQuizCommandHandler, ICommandHandler[EditQuizQuestionCommand, None]):
    async def handle(self, command: EditQuizQuestionCommand) -> None:
        async with self._uow:
            quiz = await self._get_quiz(command.quiz_id)

            quiz.edit_question(
                question_id=command.question_id,
                new_text=command.text,
                new_notice=command.notice
            )

            await self._save_quiz(quiz)
