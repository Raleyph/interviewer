from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.persistence.pg.session import get_session

SessionDep = Annotated[AsyncSession, Depends(get_session)]
