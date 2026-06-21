from sqlalchemy.ext.asyncio import AsyncSession

from src.application.shared.interfaces import IUnitOfWork, IDbContext

from src.infrastructure.persistence.pg.db_context import PostgreSqlDbContext


class PostgreSqlUnitOfWork(IUnitOfWork):
    def __init__(self, session_factory):
        self._session_factory = session_factory
        self._session: AsyncSession | None = None
        self._context: PostgreSqlDbContext | None = None

    @property
    def context(self) -> IDbContext | None:
        return self._context

    async def __aenter__(self) -> "PostgreSqlUnitOfWork":
        self._session = self._session_factory()
        self._context = PostgreSqlDbContext(self._session)
        await self._session.begin()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        try:
            if exc_type is not None:
                await self.rollback()
            else:
                await self.commit()
        finally:
            await self._session.close()

            self._session = None
            self._context = None

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
