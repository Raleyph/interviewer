from sqlalchemy import select

from src.domain.user import IUserRepository

from src.application.user.read_repository import IUserReadRepository
from src.application.user.dto import UserLookupDTO

from src.infrastructure.persistence.pg.shared import PostgreSqlRepository
from src.infrastructure.persistence.pg.user.model import UserORM


class UserRepository(PostgreSqlRepository, IUserRepository):
    pass


class UserReadRepository(PostgreSqlRepository, IUserReadRepository):
    async def get_by_username(self, username: str) -> UserLookupDTO | None:
        stmt = (
            select(
                UserORM.id,
                UserORM.username
            )
            .where(UserORM.username == username)
        )

        result = await self._session.execute(stmt)
        row = result.mappings().one_or_none()

        if row is None:
            return None

        return UserLookupDTO(**row)
