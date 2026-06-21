from typing import Annotated

from fastapi import Depends

from src.application.quiz.read_repository import IQuizReadRepository
from src.application.quiz.create.handler import CreateQuizCommandHandler
from src.application.quiz.get_by_id.handler import GetQuizByIdQueryHandler

from src.infrastructure.persistence.pg.quiz.repositories import QuizReadRepository

from src.presentation.rest.v1.shared.unit_of_work import UowDep
from src.presentation.rest.v1.shared.database import SessionDep
from src.presentation.rest.v1.user.dependencies import UserReadRepositoryDep


def get_quiz_read_repository(session: SessionDep) -> IQuizReadRepository:
    return QuizReadRepository(session)


def get_create_quiz_handler(
        uow: UowDep,
        user_read_repository: UserReadRepositoryDep
) -> CreateQuizCommandHandler:
    return CreateQuizCommandHandler(uow, user_read_repository)


def get_get_by_id_quiz_handler(
        repo: Annotated[IQuizReadRepository, Depends(get_quiz_read_repository)]
) -> GetQuizByIdQueryHandler:
    return GetQuizByIdQueryHandler(repo)


CreateQuizHandlerDep = Annotated[CreateQuizCommandHandler, Depends(get_create_quiz_handler)]
GetQuizByIdHandlerDep = Annotated[GetQuizByIdQueryHandler, Depends(get_get_by_id_quiz_handler)]
