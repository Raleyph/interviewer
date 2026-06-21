from uuid import UUID

from fastapi import APIRouter

from src.application.quiz.create.command import CreateQuizCommand
from src.application.quiz.get_by_id.query import GetQuizByIdQuery

from src.presentation.rest.v1.quiz.schemas import CreateQuizSchema
from src.presentation.rest.v1.quiz.dependencies import CreateQuizHandlerDep, GetQuizByIdHandlerDep
from src.presentation.rest.v1.auth.dependencies import CurrentUserDep

router = APIRouter(prefix="/quizzies", tags=["quizzies"])


@router.post("/")
async def create_quiz(
        schema: CreateQuizSchema,
        handler: CreateQuizHandlerDep,
        current_user: CurrentUserDep
):
    command = CreateQuizCommand(
        interviewer_id=current_user.id,
        respondent_username=schema.respondent_username,
        title=schema.title
    )

    return await handler.handle(command)


@router.get("/{quiz_id}")
async def get_quiz(
        quiz_id: UUID,
        handler: GetQuizByIdHandlerDep
):
    query = GetQuizByIdQuery(quiz_id=quiz_id)
    return await handler.handle(query)
