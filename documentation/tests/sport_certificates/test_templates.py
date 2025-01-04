from django.test import TestCase
from django.urls import reverse
from datetime import date
from documentation.models import SportCertificate
from profiles.models import SportDoctor


class SportCertificateTemplatesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create initial data for template testing."""
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

    # Test List Template
    def test_sport_certificate_list_template(self):
        """Test that the sport certificate list template is rendered correctly."""
        url = reverse('sport_certificate_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'documentation/sport_certificate_list.html')

    # Test Detail Template
    def test_sport_certificate_detail_template(self):
        """Test that the sport certificate detail template is rendered correctly."""
        url = reverse('sport_certificate_detail', kwargs={'pk': self.certificate.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'documentation/sport_certificate_detail.html')

    # Test Form Template
    def test_sport_certificate_form_template(self):
        """Test that the sport certificate form template is rendered correctly."""
        url = reverse('sport_certificate_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'documentation/sport_certificate_form.html')

    # Test Delete Template
    def test_sport_certificate_confirm_delete_template(self):
        """Test that the sport certificate delete template is rendered correctly."""
        url = reverse('sport_certificate_delete', kwargs={'pk': self.certificate.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'documentation/sport_certificate_confirm_delete.html')

