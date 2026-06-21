from uuid import UUID

from src.domain.shared.entity import Entity
from src.domain.quiz.exceptions import QuizAlreadyCompletedException, EmptyQuizException
from src.domain.question.model import Question


class Quiz(Entity):
    def __init__(
            self,
            interviewer_id: UUID,
            respondent_id: UUID,
            is_completed: bool = False,
            id_: UUID | None = None
    ):
        super().__init__(id_=id_)
        self._interviewer_id = interviewer_id
        self._respondent_id = respondent_id
        self._is_completed = is_completed
        self._questions: list[Question] = []

    # props

    @property
    def interviewer_id(self) -> UUID:
        return self._interviewer_id

    @property
    def respondent_id(self) -> UUID:
        return self._respondent_id

    @property
    def questions(self) -> tuple[Question, ...]:
        return tuple(self._questions)

    # factory

    @classmethod
    def create(cls, interviewer_id: UUID, respondent_id: UUID) -> "Quiz":
        return cls(
            interviewer_id=interviewer_id,
            respondent_id=respondent_id,
            is_completed=False
        )

    # business logic

    def add_question(self, text: str, notice: str | None = None) -> None:
        self._ensure_not_completed()
        self._questions.append(Question(text=text, notice=notice))

    def change_respondent(self, new_respondent_id: UUID) -> None:
        self._ensure_not_completed()
        self._respondent_id = new_respondent_id

    def complete(self) -> None:
        self._ensure_not_completed()
        self._ensue_not_empty()
        self._is_completed = True

    # invariants

    def _ensure_not_completed(self) -> None:
        if self._is_completed:
            raise QuizAlreadyCompletedException()

    def _ensue_not_empty(self) -> None:
        if not self._questions:
            raise EmptyQuizException()
