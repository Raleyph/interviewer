from uuid import UUID

from sqlalchemy import select

from src.domain.quiz import Quiz, IQuizRepository

from src.application.quiz.read_repository import IQuizReadRepository
from src.application.quiz.queries.get_by_id.dto import QuizDetailsDTO

from src.infrastructure.persistence.pg.shared import PostgreSqlRepository
from src.infrastructure.persistence.pg.quiz.model import QuizORM
from src.infrastructure.persistence.pg.quiz.mapper import QuizMapper


class QuizRepository(PostgreSqlRepository, IQuizRepository):
    async def get_by_id(self, id_: UUID) -> Quiz | None:
        model: QuizORM | None = await self._session.get(QuizORM, id_)

        if model is None:
            return None

        return QuizMapper.to_domain(model)

    async def add(self, entity: Quiz) -> None:
        model = QuizORM()
        QuizMapper.apply_to_model(entity, model)
        self._session.add(model)

    async def save(self, entity: Quiz) -> None:
        model: QuizORM | None = await self._session.get(QuizORM, entity.id)

        if model is None:
            raise

        QuizMapper.apply_to_model(entity, model)


class QuizReadRepository(PostgreSqlRepository, IQuizReadRepository[QuizDetailsDTO]):
    async def get_by_id(self, id_: UUID) -> QuizDetailsDTO | None:
        stmt = (
            select(
                QuizORM.id,
                QuizORM.interviewer_id,
                QuizORM.respondent_id,
                QuizORM.title,
                QuizORM.is_published
            )
            .where(QuizORM.id == id_)
        )

        result = await self._session.execute(stmt)
        row = result.mappings().one_or_none()

        if row is None:
            return None

        return QuizDetailsDTO(**row)
