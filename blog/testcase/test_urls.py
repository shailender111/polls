from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from blog.models import Question



class UrlTestCase(TestCase):
    def test_home(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        question = Question.objects.create(question_text = 'question', pub_date = timezone.now())
        url = reverse('blog:about', args=(question.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_vote(self):
        question = Question.objects.create(question_text = 'question', pub_date = timezone.now())
        url = reverse('blog:vote', args=(question.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)