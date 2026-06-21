from typing import Annotated

from fastapi import Depends

from src.application.user.read_repository import IUserReadRepository

from src.infrastructure.persistence.pg.user.repositories import UserReadRepository

from src.presentation.rest.v1.shared.database import SessionDep


def get_user_read_repository(session: SessionDep) -> IUserReadRepository:
    return UserReadRepository(session)


UserReadRepositoryDep = Annotated[IUserReadRepository, Depends(get_user_read_repository)]
