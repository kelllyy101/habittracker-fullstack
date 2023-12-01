from django.test import TestCase
from .models import Item

# Create your tests here.

class TestViews(TestCase):

    def test_habit_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'habits/habits.html')

    def test_get_add_habit_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'habits/add_habit.html')
    

    def test_edit_habit(self):
        item = Item.objects.create(name='Test Habit')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'habits/edit_habit.html')

    
    def test_can_add_habit(self):
        response = self.client.post('/add', {'name': 'Test Added Habit'})
        self.assertRedirects(response, '/')

    
    def test_can_delete_habit(self):
        item = Item.objects.create(name='Test Todo Habit')
        response = self.client.get(f'/delete/{item.id}')





