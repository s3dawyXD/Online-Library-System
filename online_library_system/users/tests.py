from django.test import TestCase


class UserViewTestCase(TestCase):
    def setUp(self):
        self.client.post(
            "/users/registration/",
            {
                "username": "testuser",
                "email": "sJ4jv@example.com",
                "password": "testpassword",
            },
        )

    def test_user_view(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200)

    def test_user_registration(self):
        response = self.client.post(
            "/users/registration/",
            {
                "username": "testuser1",
                "email": "sJ4jvv@example.com",
                "password": "testpassword",
            },
        )
        self.assertEqual(response.status_code, 201)
