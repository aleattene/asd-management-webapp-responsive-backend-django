from django.test import TestCase
from django.urls import reverse
from profiles.models import Athlete, Category


class AthleteTemplatesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create initial data for template testing."""
        cls.category = Category.objects.create(
            code='JM',
            description='Junior Maschile',
            age_range='Under 20'
        )
        cls.athlete = Athlete.objects.create(
            first_name='Mario',
            last_name='Rossi',
            date_of_birth='1990-01-01',
            place_of_birth='Rome',
            fiscal_code='RSSMRA90A01H211B',
            category=cls.category,
            trainer=None
        )

    # Test List Template
    def test_athlete_list_template(self):
        """Test that the athlete list template is rendered correctly."""
        url = reverse('athlete_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'profiles/athlete_list.html')

    # Test Detail Template
    def test_athlete_detail_template(self):
        """Test that the athlete detail template is rendered correctly."""
        url = reverse('athlete_detail', kwargs={'pk': self.athlete.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'profiles/athlete_detail.html')

    # Test Form Template
    def test_athlete_form_template(self):
        """Test that the athlete form template is rendered correctly."""
        url = reverse('athlete_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'profiles/athlete_form.html')

    # Test Delete Template
    def test_athlete_confirm_delete_template(self):
        """Test that the athlete delete template is rendered correctly."""
        url = reverse('athlete_delete', kwargs={'pk': self.athlete.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'profiles/athlete_confirm_delete.html')

