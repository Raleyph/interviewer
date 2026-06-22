from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class EditQuizQuestionCommand:
    quiz_id: UUID
    question_id: UUID
    new_text: str | None = None
    new_notice: str | None = None
