from src.domain.shared.exceptions import DomainException


class QuestionNotFoundException(DomainException):
    pass


class QuizAlreadyCompletedException(DomainException):
    pass


class QuizIsNotCompletedException(DomainException):
    pass


class EmptyQuizException(DomainException):
    pass


class NotEmptyQuizException(DomainException):
    pass
