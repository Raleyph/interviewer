from src.domain.shared.exceptions import DomainException
from src.domain.quiz.enums import QuizErrorCode


class QuizAlreadyPublishedException(DomainException):
    error_code = QuizErrorCode.QUIZ_ALREADY_PUBLISHED


class QuizIsNotPublishedException(DomainException):
    error_code = QuizErrorCode.QUIZ_NOT_PUBLISHED


class EmptyQuizException(DomainException):
    error_code = QuizErrorCode.QUIZ_EMTPY


class NotEmptyQuizException(DomainException):
    error_code = QuizErrorCode.QUIZ_NOT_EMPTY


class QuizIsAlreadyViewedException(DomainException):
    error_code = QuizErrorCode.QUIZ_ALREADY_VIEWED


class QuestionNotFoundException(DomainException):
    error_code = QuizErrorCode.QUESTION_NOT_FOUND


class QuestionAlreadyOpenedException(DomainException):
    error_code = QuizErrorCode.QUESTION_ALREADY_OPENED
