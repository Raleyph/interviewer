from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class PublishQuizCommand:
    quiz_id: UUID
