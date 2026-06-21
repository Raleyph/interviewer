from uuid import UUID

from src.domain.shared.entity import Entity
from src.domain.quiz.exceptions import (
    QuestionNotFoundException,
    QuizAlreadyPublishedException, QuizIsNotPublishedException,
    EmptyQuizException, NotEmptyQuizException
)
from src.domain.question.model import Question


class Quiz(Entity):
    def __init__(
            self,
            interviewer_id: UUID,
            respondent_id: UUID,
            title: str,
            is_published: bool = False,
            id_: UUID | None = None
    ):
        super().__init__(id_=id_)
        self._interviewer_id = interviewer_id
        self._respondent_id = respondent_id
        self._title = title
        self._is_published = is_published
        self._questions: list[Question] = []

    # props

    @property
    def interviewer_id(self) -> UUID:
        return self._interviewer_id

    @property
    def respondent_id(self) -> UUID:
        return self._respondent_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def is_published(self) -> bool:
        return self._is_published

    @property
    def questions(self) -> tuple[Question, ...]:
        return tuple(self._questions)

    # factory

    @classmethod
    def create(cls, interviewer_id: UUID, respondent_id: UUID, title: str) -> "Quiz":
        return cls(
            interviewer_id=interviewer_id,
            respondent_id=respondent_id,
            title=title,
            is_published=False
        )

    # business logic

    def _get_question_by_id(self, question_id: UUID) -> Question:
        question = next((q for q in self._questions if q.id == question_id), None)

        if not question:
            raise QuestionNotFoundException()

        return question

    def add_question(
            self,
            text: str,
            notice: str | None = None
    ) -> None:
        self._ensure_not_published()
        self._questions.append(Question(text=text, notice=notice))

    def edit_question(
            self,
            question_id: UUID,
            new_text: str | None = None,
            new_notice: str | None = None
    ) -> None:
        self._ensure_not_published()
        question = self._get_question_by_id(question_id)
        question.edit(new_text, new_notice)

    def remove_question(self, question_id: UUID,):
        self._ensure_not_published()
        question = self._get_question_by_id(question_id)
        self._questions.remove(question)

    def change_respondent(self, new_respondent_id: UUID) -> None:
        self._ensure_not_published()
        self._respondent_id = new_respondent_id

    def restore_questions(self, questions: list[Question]) -> None:
        self._ensure_not_published()
        self._ensure_is_empty()
        self._questions = questions

    def publish(self) -> None:
        self._ensure_not_published()
        self._ensure_not_empty()
        self._is_published = True

    def answer_question(self, question_id: UUID) -> None:
        self._ensure_is_published()
        question = self._get_question_by_id(question_id)
        question.answer()

    # invariants

    def _ensure_not_published(self) -> None:
        if self._is_published:
            raise QuizAlreadyPublishedException()

    def _ensure_is_published(self) -> None:
        if not self._is_published:
            raise QuizIsNotPublishedException()

    def _ensure_not_empty(self) -> None:
        if not self._questions:
            raise EmptyQuizException()

    def _ensure_is_empty(self) -> None:
        if self._questions:
            raise NotEmptyQuizException()
