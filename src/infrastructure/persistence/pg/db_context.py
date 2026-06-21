from functools import cached_property

from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.user import IUserRepository
from src.domain.quiz import IQuizRepository

from src.infrastructure.persistence.pg.user import UserRepository
from src.infrastructure.persistence.pg.quiz import QuizRepository


class PostgreSqlDbContext:
    def __init__(self, session: AsyncSession):
        self._session = session

    @cached_property
    def users(self) -> IUserRepository:
        return UserRepository(self._session)

    @cached_property
    def quizzies(self) -> IQuizRepository:
        return QuizRepository(self._session)
