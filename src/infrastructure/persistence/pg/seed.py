import asyncio
from uuid import UUID

from src.infrastructure.persistence.pg.session import async_session_factory
from src.infrastructure.persistence.pg.user.model import UserORM

DEV_USER_ID = UUID("11111111-1111-1111-1111-111111111111")


async def seed_dev_users() -> None:
    async with async_session_factory() as session:
        existing = await session.get(UserORM, DEV_USER_ID)

        if existing is not None:
            return

        user = UserORM(
            id=DEV_USER_ID,
            auth_provider="fake",
            auth_subject="dev-user",
            email="mailbox@example.com",
            username="raleyph",
            is_active=True
        )

        session.add(user)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(seed_dev_users())
