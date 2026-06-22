from uuid import UUID

from fastapi import APIRouter, status

from src.application.quiz.commands.create import CreateQuizCommand
from src.application.quiz.commands.update import UpdateQuizCommand
from src.application.quiz.commands.publish import PublishQuizCommand
from src.application.quiz.commands.add_question import AddQuizQuestionCommand
from src.application.quiz.commands.edit_question import EditQuizQuestionCommand
from src.application.quiz.commands.remove_question import RemoveQuizQuestionCommand

from src.application.quiz.queries.get_by_id import GetQuizByIdQuery

from src.presentation.rest.v1.auth.dependencies import CurrentUserDep

from src.presentation.rest.v1.quiz.schemas import (
    CreateQuizSchema,
    UpdateQuizSchema,
    AddQuizQuestionSchema,
    EditQuizQuestionSchema,
    CreateQuizResponseSchema,
    AddQuizQuestionResponseSchema
)

from src.presentation.rest.v1.quiz.dependencies import (
    CreateQuizHandlerDep,
    UpdateQuizHandlerDep,
    PublishQuizHandlerDep,
    AddQuizQuestionHandlerDep,
    EditQuizQuestionHandlerDep,
    RemoveQuizQuestionHandlerDep,
    GetQuizByIdHandlerDep
)

router = APIRouter(prefix="/quizzes", tags=["quizzes"])


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateQuizResponseSchema
)
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

    result = await handler.handle(command)
    return CreateQuizResponseSchema(id=result)


@router.patch(
    "/{quiz_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_quiz(
        quiz_id: UUID,
        schema: UpdateQuizSchema,
        handler: UpdateQuizHandlerDep
):
    command = UpdateQuizCommand(
        quiz_id=quiz_id,
        title=schema.title,
        respondent_id=schema.respondent_id
    )

    await handler.handle(command)


@router.post(
    "/{quiz_id}/publish",
    status_code=status.HTTP_204_NO_CONTENT
)
async def publish_quiz(
        quiz_id: UUID,
        handler: PublishQuizHandlerDep
):
    command = PublishQuizCommand(quiz_id=quiz_id)
    await handler.handle(command)


@router.post(
    "/{quiz_id}/questions",
    status_code=status.HTTP_201_CREATED,
    response_model=AddQuizQuestionResponseSchema
)
async def add_question(
        quiz_id: UUID,
        schema: AddQuizQuestionSchema,
        handler: AddQuizQuestionHandlerDep
):
    command = AddQuizQuestionCommand(
        quiz_id=quiz_id,
        text=schema.text,
        notice=schema.notice
    )

    result = await handler.handle(command)
    return AddQuizQuestionResponseSchema(id=result)


@router.patch(
    "/{quiz_id}/questions/{question_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def edit_question(
        quiz_id: UUID,
        question_id: UUID,
        schema: EditQuizQuestionSchema,
        handler: EditQuizQuestionHandlerDep
):
    command = EditQuizQuestionCommand(
        quiz_id=quiz_id,
        question_id=question_id,
        text=schema.text,
        notice=schema.notice
    )

    await handler.handle(command)


@router.delete(
    "/{quiz_id}/questions/{question_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def remove_question(
        quiz_id: UUID,
        question_id: UUID,
        handler: RemoveQuizQuestionHandlerDep
):
    command = RemoveQuizQuestionCommand(
        quiz_id=quiz_id,
        question_id=question_id
    )

    await handler.handle(command)


@router.get("/{quiz_id}")
async def get_quiz(
        quiz_id: UUID,
        handler: GetQuizByIdHandlerDep
):
    query = GetQuizByIdQuery(quiz_id=quiz_id)
    return await handler.handle(query)
