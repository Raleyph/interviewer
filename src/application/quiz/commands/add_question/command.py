from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class AddQuizQuestionCommand:
    quiz_id: UUID
    text: str
    notice: str | None = None
