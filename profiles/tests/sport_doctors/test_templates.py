from django.test import TestCase
from django.urls import reverse
from profiles.models import SportDoctor


class SportDoctorTemplatesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create initial data for template testing."""
        cls.sport_doctor = SportDoctor.objects.create(
            first_name='Giovanni',
            last_name='Verdi',
            vat_number='12345678901'
        )

    # Test List Template
    def test_sport_doctor_list_template(self):
        """Test that the sport doctor list template is rendered correctly."""
        url = reverse('sport_doctor_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'profiles/sport_doctor_list.html')

    # Test Detail Template
    def test_sport_doctor_detail_template(self):
        """Test that the sport doctor detail template is rendered correctly."""
        url = reverse('sport_doctor_detail', kwargs={'pk': self.sport_doctor.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'profiles/sport_doctor_detail.html')

    # Test Form Template
    def test_sport_doctor_form_template(self):
        """Test that the sport_doctor form template is rendered correctly."""
        url = reverse('sport_doctor_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'profiles/sport_doctor_form.html')

    # Test Delete Template
    def test_sport_doctor_confirm_delete_template(self):
        """Test that the sport_doctor delete template is rendered correctly."""
        url = reverse('sport_doctor_delete', kwargs={'pk': self.sport_doctor.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'profiles/sport_doctor_confirm_delete.html')