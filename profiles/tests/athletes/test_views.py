from django.test import TestCase, Client
from django.urls import reverse
from datetime import date
from profiles.models import Athlete, Category, Trainer


class AthleteViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create shared data for all tests."""
        cls.category = Category.objects.create(
            code='JM',
            description='Junior Maschile',
            age_range='Under 20'
        )
        cls.trainer = Trainer.objects.create(
            first_name='Paolo',
            last_name='Bianchi',
            fiscal_code='BNCPLO80A01H211B'
        )
        cls.athlete = Athlete.objects.create(
            first_name='Mario',
            last_name='Rossi',
            date_of_birth='1990-01-01',
            place_of_birth='Rome',
            fiscal_code='RSSMRA90A01H211B',
            category=cls.category,
            trainer=cls.trainer
        )

    def setUp(self):
        """Set up the client for testing."""
        self.client = Client()

    # Test ListView
    def test_athlete_list_view(self):
        """Test that the Athlete ListView returns a 200 status code and uses the correct template."""
        url = reverse('athlete_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/athlete_list.html')
        self.assertIn(self.athlete, response.context['athlete_list'])

    # Test DetailView
    def test_athlete_detail_view(self):
        """Test that the Athlete DetailView returns a 200 status code and displays the correct object."""
        url = reverse('athlete_detail', kwargs={"pk": self.athlete.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/athlete_detail.html')
        self.assertEqual(response.context['athlete_detail'], self.athlete)

    # Test CreateView
    def test_athlete_create_view(self):
        """Test creating a new athlete."""
        url = reverse('athlete_create')
        payload = {
            'first_name': 'Luigi',
            'last_name': 'Bianchi',
            'date_of_birth': '1995-05-15',
            'place_of_birth': 'Milan',
            'fiscal_code': 'BNCLGI95E15H211B',
            'category': self.category.pk,
            'trainer': self.trainer.pk
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Athlete.objects.count(), 2)
        new_athlete = Athlete.objects.get(fiscal_code='BNCLGI95E15H211B')
        self.assertEqual(new_athlete.first_name, 'Luigi')
        self.assertEqual(new_athlete.last_name, 'Bianchi')
        self.assertEqual(new_athlete.date_of_birth, date(1995, 5, 15))
        self.assertEqual(new_athlete.place_of_birth, 'Milan')
        self.assertEqual(new_athlete.category, self.category)
        self.assertEqual(new_athlete.trainer, self.trainer)

    # Test UpdateView
    def test_athlete_update_view(self):
        """Test updating an existing athlete."""
        url = reverse('athlete_update', kwargs={"pk": self.athlete.pk})
        payload = {
            'first_name': 'Mario Updated',
            'last_name': 'Rossi',
            'date_of_birth': '1990-01-01',
            'place_of_birth': 'Rome',
            'fiscal_code': 'RSSMRA90A01H211B',
            'category': self.category.pk,
            'trainer': self.trainer.pk
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 302)
        self.athlete.refresh_from_db()
        self.assertEqual(self.athlete.first_name, 'Mario Updated')
        self.assertEqual(self.athlete.last_name, 'Rossi')
        self.assertEqual(self.athlete.date_of_birth, date(1990, 1, 1))
        self.assertEqual(self.athlete.place_of_birth, 'Rome')
        self.assertEqual(self.athlete.category, self.category)
        self.assertEqual(self.athlete.trainer, self.trainer)

    # Test DeleteView
    def test_athlete_delete_view(self):
        """Test deleting an athlete."""
        url = reverse('athlete_delete', kwargs={"pk": self.athlete.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Athlete.objects.filter(pk=self.athlete.pk).exists())
