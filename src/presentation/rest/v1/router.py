from fastapi import APIRouter

from src.presentation.rest.v1.quiz.router import router as quiz_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(quiz_router)
