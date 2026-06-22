from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class DeleteQuizCommand:
    quiz_id: UUID
