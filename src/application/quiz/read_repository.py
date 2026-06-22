from typing import Protocol
from uuid import UUID

from src.application.quiz.queries.get_by_id.dto import QuizDetailsDTO


class IQuizReadRepository(Protocol):
    async def get_by_id(self, id_: UUID) -> QuizDetailsDTO | None: ...
