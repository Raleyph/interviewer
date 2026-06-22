from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class UpdateQuizCommand:
    quiz_id: UUID
    respondent_id: UUID | None = None
    title: str | None = None
