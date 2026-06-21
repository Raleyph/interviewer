from uuid import UUID

from src.domain.quiz import Quiz, IQuizRepository

from src.infrastructure.persistence.pg.shared import PostgreSqlRepository
from src.infrastructure.persistence.pg.quiz.model import QuizORM
from src.infrastructure.persistence.pg.quiz.mapper import QuizMapper


class QuizRepository(PostgreSqlRepository, IQuizRepository):
    async def get_by_id(self, id_: UUID) -> Quiz | None:
        model: QuizORM | None = await self._session.get(QuizORM, id_)

        if not model:
            return None

        return QuizMapper.to_domain(model)

    async def add(self, entity: Quiz) -> None:
        model = QuizORM()
        QuizMapper.apply_to_model(entity, model)
        self._session.add(model)
