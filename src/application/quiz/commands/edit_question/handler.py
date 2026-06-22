from src.application.shared.interfaces import ICommandHandler
from src.application.quiz.commands.base_handler import BaseQuizCommandHandler
from src.application.quiz.commands.edit_question.command import EditQuizQuestionCommand


class EditQuizQuestionCommandHandler(BaseQuizCommandHandler, ICommandHandler[EditQuizQuestionCommand, None]):
    async def handle(self, command: EditQuizQuestionCommand) -> None:
        quiz = await self._get_quiz(command.quiz_id)

        quiz.edit_question(
            question_id=command.question_id,
            new_text=command.new_text,
            new_notice=command.new_notice
        )

        await self._save_quiz(quiz)
