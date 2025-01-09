# from django.urls import reverse
# from django.test import TestCase
# from django.contrib.auth import get_user_model
#
#
# class UserDashboardViewTest(TestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username='test-user',
#             email='test@example.com',
#             password='secure-password-123'
#         )
#
#     def test_dashboard_access_authenticated_user(self):
#         self.client.login(username='test-user', password='secure-password-123')
#         response = self.client.get(reverse('users:dashboard'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'users/dashboard.html')
#
#     def test_dashboard_access_unauthenticated_user(self):
#         response = self.client.get(reverse('users:dashboard'))
