from typing import Protocol

from src.domain.user import IUserRepository
from src.domain.quiz import IQuizRepository


class IDbContext(Protocol):
    @property
    def users(self) -> IUserRepository: ...

    @property
    def quizzies(self) -> IQuizRepository: ...
