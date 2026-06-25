from uuid import UUID

from src.domain.quiz import Quiz
from src.domain.question import Question

from src.infrastructure.persistence.pg.quiz.model import QuizORM


class QuizMapper:
    @staticmethod
    def to_domain(model: QuizORM) -> Quiz:
        quiz = Quiz(
            id_=model.id,
            interviewer_id=model.interviewer_id,
            respondent_id=model.respondent_id,
            title=model.title,
            is_published=model.is_published,
            published_at=model.published_at,
            current_question_id=model.current_question_id
        )

        questions = [
            Question(
                id_=UUID(question_data["id"]),
                text=question_data["text"],
                notice=question_data["notice"],
                status=question_data["status"]
            )
            for question_data in model.questions_json or []
        ]

        quiz.restore_questions(questions)

        return quiz

    @staticmethod
    def apply_to_model(entity: Quiz, model: QuizORM) -> None:
        questions_json = [
            {
                "id": str(question.id),
                "text": question.text,
                "notice": question.notice,
                "status": question.status
            }
            for question in entity.questions
        ]

        model.id = entity.id
        model.interviewer_id = entity.interviewer_id
        model.respondent_id = entity.respondent_id
        model.title = entity.title
        model.is_published = entity.is_published
        model.questions_json = questions_json
        model.published_at = entity.published_at
