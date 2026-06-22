from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class ChangeQuizRespondentCommand:
    quiz_id: UUID
    new_respondent_id: UUID
