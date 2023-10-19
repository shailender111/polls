from blog.models import Question, Choice
from django.utils import timezone
from django.test import TestCase


class QuestionModel(TestCase):
    def test_question(self):
        question = Question.objects.create(question_text='question', pub_date = timezone.now())
        self.assertEqual(question.question_text, 'question')
        # print(question.pub_date)
        # self.assertEqual(question.pub_date, )

class ChoiceModel(TestCase):
    def test_choice_with_question(self):
        question = Question.objects.create(question_text='question', pub_date = timezone.now())
        choice=Choice.objects.create(question = question,choice_text = 'first')
        saved_choice = Choice.objects.get(choice_text='first')
        self.assertEqual(saved_choice.question, question)
        self.assertTrue(isinstance(question,Question))