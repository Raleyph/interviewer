from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class RenameQuizCommand:
    quiz_id: UUID
    new_title: str
