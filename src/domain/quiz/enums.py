from enum import auto

from src.domain.shared.enums import ErrorCode


class QuizErrorCode(ErrorCode):
    QUIZ_ALREADY_PUBLISHED = auto()
    QUIZ_NOT_PUBLISHED = auto()
    QUIZ_EMTPY = auto()
    QUIZ_NOT_EMPTY = auto()
    QUIZ_ALREADY_VIEWED = auto()

    QUESTION_NOT_FOUND = auto()
    QUESTION_ALREADY_OPENED = auto()
