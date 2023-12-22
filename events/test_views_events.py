from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Item

class TestViews(TestCase):

    def user_login(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

   def test_landing_view(self):
        # Test the landing view
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing.html')