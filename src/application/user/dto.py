from uuid import UUID

from pydantic import BaseModel


class UserLookupDTO(BaseModel):
    id: UUID
    username: str
