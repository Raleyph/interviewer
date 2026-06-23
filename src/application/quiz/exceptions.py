from src.application.shared.exceptions import ApplicationError


class QuizNotFoundError(ApplicationError):
    status_code = 404
