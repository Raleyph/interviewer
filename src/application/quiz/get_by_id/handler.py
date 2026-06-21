from src.application.shared.interfaces import IQueryHandler
from src.application.quiz.read_repository import IQuizReadRepository
from src.application.quiz.get_by_id.query import GetQuizByIdQuery
from src.application.quiz.get_by_id.dto import QuizDetailsDTO


class GetQuizByIdQueryHandler(IQueryHandler[GetQuizByIdQuery, QuizDetailsDTO]):
    def __init__(self, quiz_read_repository: IQuizReadRepository):
        self._read_repository = quiz_read_repository

    async def handle(self, query: GetQuizByIdQuery) -> QuizDetailsDTO | None:
        quiz = await self._read_repository.get_by_id(query.quiz_id)

        if quiz is None:
            raise

        return quiz
