from django.test import TestCase, Client
from django.urls import reverse
from datetime import date
from documentation.models import SportCertificate
from profiles.models import SportDoctor


class SportCertificateViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create initial data for all tests."""
        cls.doctor = SportDoctor.objects.create(
            first_name='Giovanni',
            last_name='Verdi',
            vat_number='12345678901'
        )
        cls.certificate = SportCertificate.objects.create(
            facility_id='FAC123',
            issued_date=date(2024, 1, 1),
            expiration_date=date(2025, 1, 1),
            doctor=cls.doctor
        )

    def setUp(self):
        self.client = Client()

    # Test ListView
    def test_sport_certificate_list_view(self):
        """Test that the sport certificate list view returns status 200 and uses the correct template."""
        url = reverse('sport_certificate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'documentation/sport_certificate_list.html')
        self.assertIn(self.certificate, response.context['sport_certificate_list'])

    # Test DetailView
    def test_sport_certificate_detail_view(self):
        """Test that the sport certificate detail view returns status 200 and displays the correct object."""
        url = reverse('sport_certificate_detail', kwargs={"pk":self.certificate.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'documentation/sport_certificate_detail.html')
        self.assertEqual(response.context['sport_certificate_detail'], self.certificate)

    # Test CreateView
    def test_sport_certificate_create_view(self):
        """Test creating a new sport certificate."""
        url = reverse('sport_certificate_create')
        payload = {
            'facility_id': 'FAC456',
            'issued_date': '2024-06-01',
            'expiration_date': '2025-06-01',
            'doctor': self.doctor.pk
        }
        response = self.client.post(url, payload)
        #
        self.assertEqual(response.status_code, 302)
        self.assertEqual(SportCertificate.objects.count(), 2)
        certificate = SportCertificate.objects.get(facility_id='FAC456')
        self.assertEqual(certificate.doctor, self.doctor)

    # Test UpdateView #
    def test_sport_certificate_update_view(self):
        """Test updating an existing sport certificate."""
        url = reverse('sport_certificate_update', kwargs={"pk": self.certificate.pk})
        payload = {
            'facility_id': 'FAC789',
            'issued_date': '2024-07-01',
            'expiration_date': '2025-07-01',
            'doctor': self.doctor.pk
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 302)
        self.certificate.refresh_from_db()
        self.assertEqual(self.certificate.facility_id, 'FAC789')

    # Test DeleteView #
    def test_sport_certificate_delete_view(self):
        """Test deleting an existing sport certificate."""
        url = reverse('sport_certificate_delete', kwargs={"pk": self.certificate.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(SportCertificate.objects.filter(pk=self.certificate.pk).exists())
