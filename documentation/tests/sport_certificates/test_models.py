from django.test import TestCase
from documentation.models import SportCertificate
from profiles.models import SportDoctor
from datetime import date


class SportCertificateModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create a valid instance of SportDoctor shared by all tests."""
        cls.sport_doctor = SportDoctor.objects.create(
            first_name='Giovanni',
            last_name='Verdi',
            vat_number='12345678901'
        )

    def setUp(self):
        """Create a valid instance of SportCertificate for each test."""
        self.certificate = SportCertificate.objects.create(
            facility_id='FAC123',
            issued_date=date(2024, 1, 1),
            expiration_date=date(2025, 1, 1),
            doctor=self.sport_doctor
        )

    def test_sport_certificate_creation(self):
        """Test that a valid SportCertificate instance is created correctly."""
        self.assertEqual(self.certificate.facility_id, 'FAC123')
        self.assertEqual(self.certificate.issued_date, date(2024, 1, 1))
        self.assertEqual(self.certificate.expiration_date, date(2025, 1, 1))
        self.assertEqual(self.certificate.doctor, self.sport_doctor)

    def test_sport_certificate_required_fields(self):
        """Test that required fields cannot be left blank."""
        pass

    def test_sport_certificate_valid_dates(self):
        """Test that issued_date must be before expiration_date."""
        pass

    def test_sport_certificate_string_representation(self):
        """Test __str__ method."""
        self.assertEqual(
            str(self.certificate),
            'Certificato FAC123 - Emesso il 2024-01-01 da Giovanni Verdi - P.IVA: 12345678901'
        )

    def test_sport_certificate_repr_representation(self):
        """Test __repr__ method."""
        self.assertEqual(
            repr(self.certificate),
            'SportCertificate(facility_id=FAC123, issued_date=2024-01-01, '
            'expiration_date=2025-01-01, doctor=Giovanni Verdi - P.IVA: 12345678901)'
        )

    def test_sport_certificate_ordering(self):
        """Test ordering."""
        pass
