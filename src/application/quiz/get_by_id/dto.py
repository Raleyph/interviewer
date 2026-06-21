from uuid import UUID

from pydantic import BaseModel


class QuizDetailsDTO(BaseModel):
    id: UUID
    interviewer_id: UUID
    responder_id: UUID
    title: str
    is_published: bool
