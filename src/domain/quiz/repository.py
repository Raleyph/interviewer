from typing import Protocol

from src.domain.shared.repository import IRepository
from src.domain.quiz import Quiz


class IQuizRepository(IRepository[Quiz], Protocol):
    async def delete(self, entity: Quiz) -> None: ...
