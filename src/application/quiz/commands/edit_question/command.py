from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class EditQuizQuestionCommand:
    quiz_id: UUID
    question_id: UUID
    text: str | None = None
    notice: str | None = None
