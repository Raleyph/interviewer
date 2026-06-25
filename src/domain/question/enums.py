from enum import StrEnum


class QuestionStatus(StrEnum):
    NEW = "new"
    OPENED = "opened"
    ANSWERED = "answered"
