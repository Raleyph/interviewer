from uuid import UUID

from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.persistence.pg.shared import Base


class QuizORM(Base):
    __tablename__ = "quizzes"

    interviewer_id: Mapped[UUID] = mapped_column(nullable=False)
    responder_id: Mapped[UUID] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)

    is_completed: Mapped[bool] = mapped_column(default=False, nullable=False)

    questions_json: Mapped[list[dict]] = mapped_column(JSON)
