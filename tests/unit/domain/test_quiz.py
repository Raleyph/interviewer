import pytest

from uuid import uuid4

from src.domain.quiz import Quiz
from src.domain.quiz.exceptions import QuestionNotFoundException


@pytest.fixture
def empty_quiz():
    return Quiz.create(interviewer_id=uuid4(), respondent_id=uuid4(), title="Test quiz")


@pytest.fixture
def quiz_with_question(empty_quiz):
    empty_quiz.add_question(text="How have you been?")
    return empty_quiz


class TestQuizAddQuestion:
    def test_add_question_success(self, empty_quiz):
        question_text = "What is your favorite color?"
        empty_quiz.add_question(text=question_text)

        assert len(empty_quiz.questions) == 1

        added_question = empty_quiz.questions[0]

        assert added_question.text == question_text
        assert added_question.is_answered is False


class TestQuizRemoveQuestion:
    def test_remove_question_success(self, quiz_with_question):
        target_question = quiz_with_question.questions[0]
        question_id = target_question.id

        quiz_with_question.remove_question(question_id=question_id)

        assert len(quiz_with_question.questions) == 0

    def test_remove_question_not_found_raises_error(self, quiz_with_question):
        wrong_id = uuid4()

        with pytest.raises(QuestionNotFoundException):
            quiz_with_question.remove_question(question_id=wrong_id)
