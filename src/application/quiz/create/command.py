from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class CreateQuizCommand:
    interviewer_id: UUID
    respondent_username: str
    title: str
