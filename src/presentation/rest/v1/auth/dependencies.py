from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException, status

from src.presentation.rest.v1.auth.current_user import CurrentUser


async def get_current_user() -> CurrentUser:
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Authentication is not configured"
    )


async def get_fake_current_user() -> CurrentUser:
    return CurrentUser(
        id=UUID("11111111-1111-1111-1111-111111111111"),
        email="mailbox@example.com",
        username="raleyph"
    )


CurrentUserDep = Annotated[CurrentUser, Depends(get_current_user)]
