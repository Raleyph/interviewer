from typing import Protocol
from uuid import UUID

from pydantic import BaseModel


class IQuizReadRepository[TResult: BaseModel](Protocol):
    async def get_by_id(self, id_: UUID) -> TResult | None: ...
