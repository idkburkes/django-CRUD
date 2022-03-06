from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack


class MovieTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test-user", email="test@gmail.com", password="password"
        )

        self.snack = Snack.objects.create(
            title="Test Snack", description="This is a test snack", purchaser=self.user
        )

    def test_string_representation(self):
        self.assertEquals(str(self.snack), "Test Snack")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "Test Snack")
        self.assertEqual(f"{self.snack.purchaser}", "test-user")
        self.assertEqual(f"{self.snack.description}", "description test")

    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Snack")
        self.assertTemplateUsed(response, "snack_list.html")

    