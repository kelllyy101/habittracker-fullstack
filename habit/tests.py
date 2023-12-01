from django.test import TestCase
from .models import Item

# Create your tests here.

class TestViews(TestCase):

    def test_habit_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'habit/habits.html')

