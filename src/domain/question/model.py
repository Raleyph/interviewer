from datetime import datetime
from uuid import UUID

from src.domain.shared.entity import Entity
from src.domain.question.enums import QuestionStatus
from src.domain.question.exceptions import InvalidQuestionStateException


class Question(Entity):
    def __init__(
            self,
            text: str,
            notice: str | None = None,
            status: QuestionStatus = QuestionStatus.NEW,
            id_: UUID | None = None
    ):
        super().__init__(id_=id_)
        self._text = text
        self._notice = notice
        self._status = status
        self._opened_at: datetime | None = None

    # magic methods

    def __str__(self) -> str:
        return f"{self._text} ({self._notice})"

    # props

    @property
    def text(self) -> str:
        return self._text

    @property
    def notice(self) -> str | None:
        return self._notice

    @property
    def status(self) -> QuestionStatus:
        return self._status

    @property
    def is_new(self) -> bool:
        return self._status == QuestionStatus.NEW

    @property
    def is_opened(self) -> bool:
        return self._status == QuestionStatus.OPENED

    # factory

    @classmethod
    def create(cls, text: str, notice: str | None = None) -> "Question":
        return cls(
            text=text,
            notice=notice,
            status=QuestionStatus.NEW
        )

    # business logic

    def edit(
            self,
            new_text: str | None = None,
            new_notice: str | None = None
    ) -> None:
        if new_text:
            self._text = new_text
        if new_notice:
            self._notice = new_notice

    def open(self, now: datetime) -> None:
        if self._status != QuestionStatus.NEW:
            raise InvalidQuestionStateException()

        self._status = QuestionStatus.OPENED
        self._opened_at = now

    def answer(self):
        if self._status != QuestionStatus.OPENED:
            raise InvalidQuestionStateException()

        self._status = QuestionStatus.ANSWERED
