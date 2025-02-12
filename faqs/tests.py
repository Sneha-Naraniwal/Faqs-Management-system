from django.test import TestCase
from rest_framework.test import APIClient
from .models import FAQ


class FAQTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faq = FAQ.objects.create(
            question="What is Python?",
            answer="<p>Python is a programming language.</p>"
        )

    def test_get_faqs(self):
        response = self.client.get('/api/faqs/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_faq(self):
        data = {
            "question": "What is Django?",
            "answer": "<p>Django is a Python framework.</p>"
        }
        response = self.client.post('/api/faqs/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(FAQ.objects.count(), 2)

    def test_translation_api(self):
        response = self.client.get('/api/faqs/?lang=bn')
        self.assertEqual(response.status_code, 200)
        self.assertIn('question', response.data[0])
