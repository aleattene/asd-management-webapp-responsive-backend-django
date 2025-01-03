from django.test import TestCase
from profiles.models import SportDoctor


class SportDoctorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create a valid instance of SportDoctor shared by all tests."""
        cls.sport_doctor = SportDoctor.objects.create(
            first_name='Giovanni',
            last_name='Verdi',
            vat_number='12345678901'
        )

    def test_sport_doctor_creation(self):
        """Test that a valid SportDoctor instance is created correctly."""
        self.assertEqual(self.sport_doctor.first_name, 'Giovanni')
        self.assertEqual(self.sport_doctor.last_name, 'Verdi')
        self.assertEqual(self.sport_doctor.vat_number, '12345678901')

    def test_required_fields(self):
        """Test that required fields cannot be left blank."""
        pass

    def test_vat_number_uniqueness(self):
        """Test that the vat_number field is unique."""
        pass

    def test_vat_number_length(self):
        """Test that vat_number respects the max_length."""
        pass

    def test_sport_doctor_string_representation(self):
        """Test __str__ method."""
        self.assertEqual(
            str(self.sport_doctor),
            'Giovanni Verdi - P.IVA: 12345678901'
        )

    def test_sport_doctor_repr_representation(self):
        """Test __repr__ method."""
        self.assertEqual(
            repr(self.sport_doctor),
            'SportDoctor(first_name=Giovanni, last_name=Verdi, vat_number=12345678901)'
        )

    def test_ordering(self):
        pass




