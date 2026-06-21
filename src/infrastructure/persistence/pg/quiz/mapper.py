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
            respondent_id=model.responder_id,
            is_completed=model.is_completed
        )

        questions = [
            Question(
                id_=UUID(question_data["id"]),
                text=question_data["text"],
                notice=question_data["notice"],
                is_answered=question_data["is_answered"]
            )
            for question_data in model.questions_json
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
                "is_answered": question.is_answered
            }
            for question in entity.questions
        ]

        model.id = entity.id
        model.interviewer_id = entity.interviewer_id
        model.responder_id = entity.respondent_id
        model.is_completed = entity.is_completed
        model.questions_json = questions_json
