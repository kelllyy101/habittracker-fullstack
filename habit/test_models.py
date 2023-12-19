from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_habit_string_method_returns_name(self):
        item = Item.objects.create(name='Test Habit')
        self.assertEqual(str(item), 'Test Habit')
