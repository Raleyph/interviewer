from typing import Annotated

from fastapi import Depends

from src.application.quiz.read_repository import IQuizReadRepository

from src.application.quiz.commands.create import CreateQuizCommandHandler
from src.application.quiz.commands.update import UpdateQuizCommandHandler
from src.application.quiz.commands.delete import DeleteQuizCommandHandler
from src.application.quiz.commands.publish import PublishQuizCommandHandler
from src.application.quiz.commands.rollback import RollbackQuizCommandHandler
from src.application.quiz.commands.add_question import AddQuizQuestionCommandHandler
from src.application.quiz.commands.edit_question import EditQuizQuestionCommandHandler
from src.application.quiz.commands.remove_question import RemoveQuizQuestionCommandHandler

from src.application.quiz.queries.get_by_id import GetQuizByIdQueryHandler

from src.infrastructure.persistence.pg.quiz.repositories import QuizReadRepository

from src.presentation.rest.v1.shared.dependencies import SessionDep, UowDep
from src.presentation.rest.v1.user.dependencies import UserReadRepositoryDep


def get_quiz_read_repository(session: SessionDep) -> IQuizReadRepository:
    return QuizReadRepository(session)


# commands

def get_create_quiz_handler(
        uow: UowDep,
        user_read_repository: UserReadRepositoryDep
) -> CreateQuizCommandHandler:
    return CreateQuizCommandHandler(uow, user_read_repository)


def get_update_quiz_handler(uow: UowDep) -> UpdateQuizCommandHandler:
    return UpdateQuizCommandHandler(uow)


def get_delete_quiz_handler(uow: UowDep) -> DeleteQuizCommandHandler:
    return DeleteQuizCommandHandler(uow)


def get_publish_quiz_handler(uow: UowDep) -> PublishQuizCommandHandler:
    return PublishQuizCommandHandler(uow)


def get_rollback_quiz_handler(uow: UowDep) -> RollbackQuizCommandHandler:
    return RollbackQuizCommandHandler(uow)


def get_add_quiz_question_handler(uow: UowDep) -> AddQuizQuestionCommandHandler:
    return AddQuizQuestionCommandHandler(uow)


def get_edit_quiz_question_handler(uow: UowDep) -> EditQuizQuestionCommandHandler:
    return EditQuizQuestionCommandHandler(uow)


def get_remove_quiz_question_handler(uow: UowDep) -> RemoveQuizQuestionCommandHandler:
    return RemoveQuizQuestionCommandHandler(uow)


# queries

def get_get_by_id_quiz_handler(
        repo: Annotated[IQuizReadRepository, Depends(get_quiz_read_repository)]
) -> GetQuizByIdQueryHandler:
    return GetQuizByIdQueryHandler(repo)


CreateQuizHandlerDep = Annotated[CreateQuizCommandHandler, Depends(get_create_quiz_handler)]
UpdateQuizHandlerDep = Annotated[UpdateQuizCommandHandler, Depends(get_update_quiz_handler)]
DeleteQuizHandlerDep = Annotated[DeleteQuizCommandHandler, Depends(get_delete_quiz_handler)]

PublishQuizHandlerDep = Annotated[PublishQuizCommandHandler, Depends(get_publish_quiz_handler)]
RollbackQuizHandlerDep = Annotated[RollbackQuizCommandHandler, Depends(get_rollback_quiz_handler)]

AddQuizQuestionHandlerDep = Annotated[AddQuizQuestionCommandHandler, Depends(get_add_quiz_question_handler)]
EditQuizQuestionHandlerDep = Annotated[EditQuizQuestionCommandHandler, Depends(get_edit_quiz_question_handler)]
RemoveQuizQuestionHandlerDep = Annotated[RemoveQuizQuestionCommandHandler, Depends(get_remove_quiz_question_handler)]

GetQuizByIdHandlerDep = Annotated[GetQuizByIdQueryHandler, Depends(get_get_by_id_quiz_handler)]
