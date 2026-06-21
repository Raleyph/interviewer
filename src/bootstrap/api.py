from fastapi import FastAPI

from src.infrastructure.config.settings import get_settings

from src.presentation.rest.v1.router import api_router
from src.presentation.rest.v1.auth.dependencies import get_current_user, get_fake_current_user

settings = get_settings()

app = FastAPI()

if settings.AUTH_MODE == "fake":
    app.dependency_overrides[get_current_user] = get_fake_current_user

app.include_router(api_router)
