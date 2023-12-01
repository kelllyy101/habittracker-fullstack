from django.test import TestCase
from .models import Item

# Create your tests here.

class TestViews(TestCase):

    def test_habit_list(self):
        # Test to view/get habits
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'habits/habits.html')

    def test_get_add_habit_page(self):
        # Test to add habits from add_habit.html and it saves
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'habits/add_habit.html')
    

    def test_edit_habit(self):
        # Test to edit habit and it saves
        item = Item.objects.create(name='Test Habit')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'habits/edit_habit.html')

    
    def test_can_add_habit(self):
        response = self.client.post('/add', {'name': 'Test Added Habit'})
        self.assertRedirects(response, '/')

    
    def test_can_delete_habit(self):
        # Test that deleted habits are deleted
        item = Item.objects.create(name='Test Todo Habit')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)


    def test_can_toggle_habit(self):
        # Test to toggle habit
        item = Item.objects.create(name='Test Habit', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)


    def test_can_edit_habit_redirect(self):
        # Test redirect to main page / get_habits after habit is updated
        item = Item.objects.create(name='Test Habit')
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')


    def test_add_habit_view_get(self):
        # Test the GET request for the add_habit view
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'habits/habits.html')
        self.assertIsInstance(response.context['form'], Item)


    def test_add_habit_view_post_invalid_form(self):
        # Test the POST request with an invalid form submission
        data = {'name': '', 'description': 'Invalid habit'}
        response = self.client.post(('add_habit'), data)
        self.assertEqual(response.status_code, 404)
        # Verify that no habit was added to the database
        self.assertEqual(Item.objects.count(), 0)


