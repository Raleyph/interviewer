from typing import Annotated

from fastapi import Depends

from src.application.shared.interfaces import IUnitOfWork

from src.infrastructure.persistence.pg.session import async_session_factory
from src.infrastructure.persistence.pg.unit_of_work import PostgreSqlUnitOfWork


def get_uow() -> IUnitOfWork:
    return PostgreSqlUnitOfWork(async_session_factory)


UowDep = Annotated[IUnitOfWork, Depends(get_uow)]
