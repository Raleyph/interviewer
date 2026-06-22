from uuid import UUID

from pydantic import BaseModel


# requests

class CreateQuizSchema(BaseModel):
    respondent_username: str
    title: str


class UpdateQuizSchema(BaseModel):
    respondent_id: UUID | None = None
    title: str | None = None


class AddQuizQuestionSchema(BaseModel):
    text: str
    notice: str | None = None


class EditQuizQuestionSchema(BaseModel):
    text: str | None = None
    notice: str | None = None


# responses

class CreateQuizResponseSchema(BaseModel):
    id: UUID


class AddQuizQuestionResponseSchema(BaseModel):
    id: UUID
