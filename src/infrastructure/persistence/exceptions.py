from uuid import UUID

from src.infrastructure.exceptions import InfrastructureError


class PersistenceError(InfrastructureError):
    pass


class EntityNotFoundForSaveError(PersistenceError):
    def __init__(self, entity_id: UUID):
        self._entity_id = entity_id
        super().__init__(
            f"Entity with id {entity_id} was not found during save operation"
        )
