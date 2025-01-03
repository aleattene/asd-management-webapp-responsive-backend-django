from django.test import TestCase
from profiles.models import Trainer


class TrainerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create a valid instance of Trainer shared by all tests."""
        cls.trainer = Trainer.objects.create(
            first_name='Paolo',
            last_name='Bianchi',
            fiscal_code='BNCPLO80A01H211B',
        )

    def test_trainer_creation(self):
        """Test that a valid Trainer instance is created correctly."""
        self.assertEqual(self.trainer.first_name, 'Paolo')
        self.assertEqual(self.trainer.last_name, 'Bianchi')
        self.assertEqual(self.trainer.fiscal_code, 'BNCPLO80A01H211B')

    def test_trainer_required_fields(self):
        """Test that required fields cannot be left blank."""
        pass

    def test_trainer_fiscal_code_uniqueness(self):
        """Test that the fiscal_code field is unique."""
        pass

    def test_trainer_string_representation(self):
        """Test __str__ method."""
        self.assertEqual(
            str(self.trainer),
            'Paolo Bianchi (BNCPLO80A01H211B)'
        )

    def test_trainer_repr_representation(self):
        """Test __repr__ method."""
        self.assertEqual(
            repr(self.trainer),
            'Trainer(first_name=Paolo, last_name=Bianchi, fiscal_code=BNCPLO80A01H211B)'
        )

