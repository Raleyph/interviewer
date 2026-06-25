from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.domain.shared.enums import ErrorCode
from src.domain.shared.exceptions import DomainException
from src.domain.quiz.enums import QuizErrorCode

from src.application.shared.exceptions import ApplicationError
from src.infrastructure.exceptions import InfrastructureError

type AppException = DomainException | ApplicationError | InfrastructureError

DOMAIN_STATUS_MAP: dict[ErrorCode, int] = {
    QuizErrorCode.QUIZ_ALREADY_PUBLISHED: 409,
    QuizErrorCode.QUIZ_NOT_PUBLISHED: 400,
    QuizErrorCode.QUIZ_EMTPY: 400,
    QuizErrorCode.QUIZ_NOT_EMPTY: 400,
    QuizErrorCode.QUIZ_ALREADY_VIEWED: 409,

    QuizErrorCode.QUESTION_NOT_FOUND: 404,
    QuizErrorCode.QUESTION_ALREADY_OPENED: 409
}


def build_response(exc: AppException) -> JSONResponse:
    message = (
        str(exc)
        if getattr(exc, "expose_message", False)
        else "Internal server error"
    )

    if isinstance(exc, DomainException):
        status_code = DOMAIN_STATUS_MAP.get(exc.error_code, 400)
    else:
        status_code = exc.status_code

    return JSONResponse(
        status_code=status_code,
        content={
            "error": {
                "type": type(exc).__name__,
                "message": message
            }
        }
    )


def register_exception_handler(app: FastAPI):
    @app.exception_handler(DomainException)
    async def handle_domain_error(
            _: Request,
            exc: DomainException
    )-> JSONResponse:
        return build_response(exc)

    @app.exception_handler(ApplicationError)
    async def handle_application_error(
            _: Request,
            exc: ApplicationError
    ) -> JSONResponse:
        return build_response(exc)

    @app.exception_handler(InfrastructureError)
    async def handle_infrastructure_error(
            _: Request,
            exc: InfrastructureError
    ) -> JSONResponse:
        return build_response(exc)
