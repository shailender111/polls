from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
import datetime
from blog.models import Question, Choice




def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewtest(TestCase):
    def test_case_no_poll(self):
        response = self.client.get(reverse('blog:home'))
        # print(response.context)
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, True)
        self.assertQuerySetEqual(response.context['latest_question_list'],[])
        print("..........")

    def test_past_question(self):
        question = create_question(question_text="past question", days=-30)
        response = self.client.get(reverse('blog:home'))
        self.assertQuerySetEqual(response.context["latest_question_list"], [question])

    def test_future_case(self):
        question=create_question(question_text='future question', days=30)
        response = self.client.get(reverse('blog:home'))
        # print(response)
        # self.assertContains(response, 'No questions are available')
        self.assertQuerySetEqual(response.context['latest_question_list'], [])

    def test_two_question(self):
        question1 = create_question(question_text="first question", days=-15)
        question2 = create_question(question_text="second questions", days=-10)
        response = self.client.get(reverse('blog:home'))
        self.assertQuerySetEqual(response.context['latest_question_list'], [question2,question1])


class QuestionDetailView(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text="future question", days = 15)
        url = reverse('blog:about', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_past_questions(self):
        past_question = create_question(question_text='past questions', days=-4)

        url = reverse('blog:about', args=(past_question.id,))

        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


