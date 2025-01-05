from django.test import TestCase, Client
from django.urls import reverse
from profiles.models import Trainer


class TrainerViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create shared data for all tests."""
        cls.trainer = Trainer.objects.create(
            first_name='Paolo',
            last_name='Bianchi',
            fiscal_code='BNCPLO80A01H211B'
        )

    def setUp(self):
        """Set up the client for testing."""
        self.client = Client()

    # Test ListView
    def test_trainer_list_view(self):
        """Test that the Trainer ListView returns a 200 status code and uses the correct template."""
        url = reverse('trainer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/trainer_list.html')
        self.assertIn(self.trainer, response.context['trainer_list'])

    # Test DetailView
    def test_trainer_detail_view(self):
        """Test that the Trainer DetailView returns a 200 status code and displays the correct object."""
        url = reverse('trainer_detail', kwargs={"pk": self.trainer.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/trainer_detail.html')
        self.assertEqual(response.context['trainer_detail'], self.trainer)

    # Test CreateView
    def test_trainer_create_view(self):
        """Test creating a new trainer."""
        url = reverse('trainer_create')
        payload = {
            'first_name': 'Luigi',
            'last_name': 'Bianchi',
            'fiscal_code': 'BNCLGI95E15H211B',
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Trainer.objects.count(), 2)
        new_trainer = Trainer.objects.get(fiscal_code='BNCLGI95E15H211B')
        self.assertEqual(new_trainer.first_name, 'Luigi')
        self.assertEqual(new_trainer.last_name, 'Bianchi')

    # Test UpdateView
    def test_trainer_update_view(self):
        """Test updating an existing trainer."""
        url = reverse('trainer_update', kwargs={"pk": self.trainer.pk})
        payload = {
            'first_name': 'Mario Updated',
            'last_name': 'Rossi',
            'fiscal_code': 'RSSMRA90A01H211C',
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 302)  # Redirect after update
        self.trainer.refresh_from_db()
        self.assertEqual(self.trainer.first_name, 'Mario Updated')
        self.assertEqual(self.trainer.last_name, 'Rossi')
        self.assertEqual(self.trainer.fiscal_code, 'RSSMRA90A01H211C')

    # Test DeleteView
    def test_trainer_delete_view(self):
        """Test deleting a trainer."""
        url = reverse('trainer_delete', kwargs={"pk": self.trainer.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Trainer.objects.filter(pk=self.trainer.pk).exists())
