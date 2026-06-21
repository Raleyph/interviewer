from uuid import UUID, uuid4

from src.domain.shared.event import DomainEvent


class Entity:
    def __init__(self, id_: UUID | None = None):
        self._id = id_ or uuid4()
        self._events: list[DomainEvent] = []

    # props

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def events(self) -> list[DomainEvent]:
        return self._events

    # domain logic

    def add_event(self, event: DomainEvent) -> None:
        self._events.append(event)

    def pull_events(self) -> list[DomainEvent]:
        events = self._events.copy()
        self._events.clear()
        return events

    # magic methods

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return False

        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self._id)
