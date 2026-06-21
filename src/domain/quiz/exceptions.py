from src.domain.shared.exceptions import DomainException


class QuestionNotFoundException(DomainException):
    pass


class QuizAlreadyPublishedException(DomainException):
    pass


class QuizIsNotPublishedException(DomainException):
    pass


class EmptyQuizException(DomainException):
    pass


class NotEmptyQuizException(DomainException):
    pass
