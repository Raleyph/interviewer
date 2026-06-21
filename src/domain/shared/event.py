from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True, kw_only=True)
class DomainEvent:
    id: UUID
    occurred_at: datetime
    correlation_id: UUID | None = None
    causation_id: UUID | None = None

    def to_payload(self) -> dict:
        return {
            "occurred_at": self.occurred_at.isoformat(),
            "correlation_id": str(self.correlation_id) if self.correlation_id else None,
            "causation_id": str(self.causation_id) if self.causation_id else None
        }
