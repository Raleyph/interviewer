from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class RollbackQuizCommand:
    quiz_id: UUID
