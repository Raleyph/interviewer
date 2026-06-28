from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class QuizDetailsDTO(BaseModel):
    id: UUID
    interviewer_id: UUID
    respondent_id: UUID
    title: str
    is_published: bool
    published_at: datetime | None
    current_question_id: UUID | None
