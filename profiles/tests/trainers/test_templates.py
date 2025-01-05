from django.test import TestCase
from django.urls import reverse
from profiles.models import Trainer


class TrainerTemplatesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create initial data for template testing."""
        cls.trainer = Trainer.objects.create(
            first_name='Giovanni',
            last_name='Verdi',
            fiscal_code='ABCDEF12G34H567I',
        )

    # Test List Template
    def test_trainer_list_template(self):
        """Test that the trainer list template is rendered correctly."""
        url = reverse('trainer_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'profiles/trainer_list.html')

    # Test Detail Template
    def test_trainer_detail_template(self):
        """Test that the trainer detail template is rendered correctly."""
        url = reverse('trainer_detail', kwargs={'pk': self.trainer.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'profiles/trainer_detail.html')

    # Test Form Template
    def test_trainer_form_template(self):
        """Test that the trainer form template is rendered correctly."""
        url = reverse('trainer_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'profiles/trainer_form.html')

    # Test Delete Template
    def test_trainer_confirm_delete_template(self):
        """Test that the trainer delete template is rendered correctly."""
        url = reverse('trainer_delete', kwargs={'pk': self.trainer.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'profiles/trainer_confirm_delete.html')
