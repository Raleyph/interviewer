from datetime import datetime
from uuid import UUID

from src.domain.shared.entity import Entity
from src.domain.quiz.exceptions import (
    QuestionNotFoundException,
    QuizAlreadyPublishedException,
    QuizIsNotPublishedException,
    EmptyQuizException,
    NotEmptyQuizException,
    QuestionAlreadyOpenedException,
    QuizIsAlreadyViewedException
)
from src.domain.question.model import Question


class Quiz(Entity):
    def __init__(
            self,
            interviewer_id: UUID,
            respondent_id: UUID,
            title: str,
            is_published: bool = False,
            published_at: datetime | None = None,
            current_question_id: UUID | None = None,
            id_: UUID | None = None
    ):
        super().__init__(id_=id_)
        self._interviewer_id = interviewer_id
        self._respondent_id = respondent_id
        self._title = title
        self._is_published = is_published

        self._questions: list[Question] = []

        self._published_at = published_at
        self._current_question_id = current_question_id

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

    @property
    def published_at(self) -> datetime | None:
        return self._published_at

    @property
    def current_question_id(self) -> UUID | None:
        return self._current_question_id

    # factory

    @classmethod
    def create(cls, interviewer_id: UUID, respondent_id: UUID, title: str) -> "Quiz":
        return cls(
            interviewer_id=interviewer_id,
            respondent_id=respondent_id,
            title=title,
            is_published=False
        )

    # business logic [update]

    def change_respondent(self, new_respondent_id: UUID) -> None:
        self._ensure_not_published()
        self._respondent_id = new_respondent_id

    def rename(self, new_title: str) -> None:
        self._ensure_not_published()
        self._title = new_title

    # business logic [questions]

    def _get_question_by_id(self, question_id: UUID) -> Question:
        question = next((q for q in self._questions if q.id == question_id), None)

        if not question:
            raise QuestionNotFoundException()

        return question

    def add_question(
            self,
            text: str,
            notice: str | None = None
    ) -> UUID:
        self._ensure_not_published()
        question = Question.create(text=text, notice=notice)
        self._questions.append(question)
        return question.id

    def edit_question(
            self,
            question_id: UUID,
            new_text: str | None = None,
            new_notice: str | None = None
    ) -> None:
        self._ensure_not_published()
        question = self._get_question_by_id(question_id)
        question.edit(new_text, new_notice)

    def remove_question(self, question_id: UUID):
        self._ensure_not_published()
        question = self._get_question_by_id(question_id)
        self._questions.remove(question)

    def restore_questions(self, questions: list[Question]) -> None:
        self._ensure_not_published()
        self._ensure_is_empty()
        self._questions = questions

    # business logic [answering]

    def open_next_question(self, now: datetime) -> Question:
        self._ensure_is_published()

        question = next((q for q in self._questions if q.is_new), None)

        if question is None:
            raise QuestionNotFoundException()

        question.open(now)
        self._current_question_id = question.id

        return question

    def answer_current_question(self) -> None:
        self._ensure_is_published()
        self._ensure_no_current_question()

        question = self._get_question_by_id(self._current_question_id)
        question.answer()

        self._current_question_id = None

    # business logic [publication]

    def publish(self, now: datetime) -> None:
        self._ensure_not_published()
        self._ensure_not_empty()
        self._is_published = True
        self._published_at = now
    
    def rollback(self) -> None:
        self._ensure_is_published()
        self._ensure_no_opened_questions()
        self._is_published = False
        self._published_at = None

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

    def _ensure_no_current_question(self) -> None:
        if self._current_question_id is not None:
            raise QuestionAlreadyOpenedException()

    def _ensure_no_opened_questions(self) -> None:
        if any(q.is_opened for q in self._questions):
            raise QuizIsAlreadyViewedException()
