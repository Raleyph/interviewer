from uuid import UUID

from src.domain.shared.entity import Entity


class Question(Entity):
    def __init__(
            self,
            text: str,
            notice: str | None = None,
            is_answered: bool = False,
            id_: UUID | None = None
    ):
        super().__init__(id_=id_)
        self._text = text
        self._notice = notice
        self._is_answered = is_answered

    # props

    @property
    def text(self) -> str:
        return self._text

    @property
    def notice(self) -> str | None:
        return self._notice

    @property
    def is_answered(self) -> bool:
        return self._is_answered

    # business logic

    def answer(self) -> None:
        self._is_answered = True
