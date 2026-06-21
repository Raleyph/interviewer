from src.domain.shared.exceptions import DomainException


class QuizAlreadyCompletedException(DomainException):
    pass


class EmptyQuizException(DomainException):
    pass
