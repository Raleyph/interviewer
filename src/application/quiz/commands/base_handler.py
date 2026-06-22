from uuid import UUID

from src.domain.quiz import Quiz

from src.application.shared.interfaces import IUnitOfWork


class BaseQuizCommandHandler:
    def __init__(self, uow: IUnitOfWork):
        self._uow = uow

    async def _get_quiz(self, quiz_id: UUID) -> Quiz:
        quiz = await self._uow.context.quizzies.get_by_id(quiz_id)

        if quiz is None:
            raise

        return quiz

    async def _save_quiz(self, quiz: Quiz) -> None:
        await self._uow.context.quizzies.save(quiz)
