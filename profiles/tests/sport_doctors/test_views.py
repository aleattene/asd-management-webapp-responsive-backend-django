from django.test import TestCase, Client
from django.urls import reverse
from datetime import date
from profiles.models import SportDoctor


class SportDoctorViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create shared data for all tests."""
        cls.sport_doctor = SportDoctor.objects.create(
            first_name='Giovanni',
            last_name='Verdi',
            vat_number='12345678901'
        )

    def setUp(self):
        """Set up the client for testing."""
        self.client = Client()

    # Test ListView
    def test_sport_doctor_list_view(self):
        """Test that the Sport Doctor ListView returns a 200 status code and uses the correct template."""
        url = reverse('sport_doctor_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/sport_doctor_list.html')
        self.assertIn(self.sport_doctor, response.context['sport_doctor_list'])

    # Test DetailView
    def test_sport_doctor_detail_view(self):
        """Test that the Sport Doctor DetailView returns a 200 status code and displays the correct object."""
        url = reverse('sport_doctor_detail', kwargs={"pk": self.sport_doctor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/sport_doctor_detail.html')
        self.assertEqual(response.context['sport_doctor_detail'], self.sport_doctor)

    # Test CreateView
    def test_sport_doctor_create_view(self):
        """Test creating a new sport doctor."""
        url = reverse('sport_doctor_create')
        payload = {
            'first_name': 'Luigi',
            'last_name': 'Bianchi',
            'vat_number': '12345678902',
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(SportDoctor.objects.count(), 2)
        new_sport_doctor = SportDoctor.objects.get(vat_number='12345678902')
        self.assertEqual(new_sport_doctor.first_name, 'Luigi')
        self.assertEqual(new_sport_doctor.last_name, 'Bianchi')
        self.assertEqual(new_sport_doctor.vat_number, '12345678902')

    # Test UpdateView
    def test_sport_doctor_update_view(self):
        """Test updating an existing sport doctor."""
        url = reverse('sport_doctor_update', kwargs={"pk": self.sport_doctor.pk})
        payload = {
            'first_name': 'Mario Updated',
            'last_name': 'Rossi',
            'vat_number': '12345678909',
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 302)
        self.sport_doctor.refresh_from_db()
        self.assertEqual(self.sport_doctor.first_name, 'Mario Updated')
        self.assertEqual(self.sport_doctor.last_name, 'Rossi')
        self.assertEqual(self.sport_doctor.vat_number, '12345678909')

    # Test DeleteView
    def test_sport_doctor_delete_view(self):
        """Test deleting a sport doctor."""
        url = reverse('sport_doctor_delete', kwargs={"pk": self.sport_doctor.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(SportDoctor.objects.filter(pk=self.sport_doctor.pk).exists())

