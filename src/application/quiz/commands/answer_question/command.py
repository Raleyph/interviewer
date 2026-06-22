from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class AnswerQuizQuestionCommand:
    quiz_id: UUID
    question_id: UUID
