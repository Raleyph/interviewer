from typing import Protocol
from uuid import UUID

from src.domain.shared.entity import Entity


class IRepository[TEntity: Entity](Protocol):
    async def get_by_id(self, id_: UUID) -> TEntity | None: ...
    async def add(self, entity: TEntity) -> None: ...
