from django.test import TestCase
from profiles.models.athletes import Athlete, Category
from profiles.models.trainers import Trainer


class AthleteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create a valid instance of Category and Trainer shared by all tests."""
        cls.category = Category.objects.create(
            code='JM',
            description='Junior Maschile',
            age_range='Under 20',
        )
        cls.trainer = Trainer.objects.create(
            first_name='Paolo',
            last_name='Bianchi',
            fiscal_code='BNCPLO80A01H211B',
        )

    def setUp(self):
        """Create a valid dinamic instance of Athlete for each test."""
        self.athlete = Athlete.objects.create(
            first_name='Mario',
            last_name='Rossi',
            date_of_birth='1990-01-01',
            place_of_birth='Roma',
            fiscal_code='RSSMRA90A01H211B',
            category=self.category,
        )

    def test_athlete_creation(self):
        """Test creating a new athlete without a trainer."""
        self.assertEqual(self.athlete.first_name, 'Mario')
        self.assertEqual(self.athlete.last_name, 'Rossi')
        self.assertEqual(self.athlete.date_of_birth, '1990-01-01')
        self.assertEqual(self.athlete.place_of_birth, 'Roma')
        self.assertEqual(self.athlete.fiscal_code, 'RSSMRA90A01H211B')
        self.assertEqual(self.athlete.category, self.category)
        self.assertEqual(self.athlete.category.code, 'JM')
        self.assertIsNone(self.athlete.trainer)

    def test_athlete_with_trainer(self):
        """Test creating a new athlete with a trainer."""
        self.athlete.trainer = self.trainer
        self.athlete.save()
        self.assertEqual(self.athlete.trainer, self.trainer)
        self.assertEqual(self.athlete.trainer.first_name, 'Paolo')
        self.assertEqual(self.athlete.trainer.last_name, 'Bianchi')
        self.assertEqual(self.athlete.trainer.fiscal_code, 'BNCPLO80A01H211B')

    def test_athlete_string_representation(self):
        """Test __str__ method."""
        self.assertEqual(
            str(self.athlete),
            'Mario Rossi (RSSMRA90A01H211B)'
        )

    def test__athlete_repr_representation(self):
        """Test __repr__ method."""
        self.assertEqual(
            repr(self.athlete),
            'Athlete(first_name=Mario, last_name=Rossi, date_of_birth=1990-01-01, fiscal_code=RSSMRA90A01H211B)'
        )

    def test__athlete_fiscal_code_uniqueness(self):
        """Test that the fiscal code must be unique."""
        pass

    def test__athlete_required_fields(self):
        """Test that required fields cannot be left empty."""
        pass


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create a valid instance of Category shared by all tests."""
        cls.category = Category.objects.create(
            code='AF',
            description='Allieve Femminili',
            age_range='Under 18',
        )

    def test_category_creation(self):
        """Test creating a new category."""
        self.assertEqual(self.category.code, 'AF')
        self.assertEqual(self.category.description, 'Allieve Femminili')
        self.assertEqual(self.category.age_range, 'Under 18')

    def test_category_required_fields(self):
        """Test that required fields cannot be left empty."""
        pass

    def test_category_code_uniqueness(self):
        """Test that the code must be unique."""
        pass

    def test_category_optional_age_range(self):
        """Test that the age range can be left empty."""
        category = Category.objects.create(
            code='SN',
            description='Senior',
            age_range=None
        )
        self.assertIsNone(category.age_range)

    def test_category_string_representation(self):
        """Test __str__ method."""
        self.assertEqual(
            str(self.category),
            'AF - Allieve Femminili'
        )

    def test_category_repr_representation(self):
        """Test __repr__ method."""
        self.assertEqual(
            repr(self.category),
            'Category(code=AF, description=Allieve Femminili, age_range=Under 18)'
        )

    def test_category_ordering(self):
        """Test ordering by code."""
        pass

