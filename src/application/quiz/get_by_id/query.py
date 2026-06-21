from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class GetQuizByIdQuery:
    quiz_id: UUID
