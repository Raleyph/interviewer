from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class RemoveQuizQuestionCommand:
    quiz_id: UUID
    question_id: UUID
