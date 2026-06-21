from pydantic import BaseModel


class CreateQuizSchema(BaseModel):
    respondent_username: str
    title: str
