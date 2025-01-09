from django.test import TestCase
from users.models import CustomUser


class CustomUserTest(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            username='test-user',
            email='test@example.com',
            password='secure-password-123'
        )
        self.assertEqual(user.username, 'test-user')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('secure-password-123'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = CustomUser.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin-password-987'
        )
        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.check_password('admin-password-987'))
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

