from django.db import models
from profiles.models.sport_doctors import SportDoctor


class SportCertificate(models.Model):
    facility_id = models.CharField(
        max_length=50, verbose_name="Identificativo Struttura Erogatrice"
    )
    issued_date = models.DateField(verbose_name="Data di Emissione")
    expiration_date = models.DateField(verbose_name="Data di Scadenza")
    doctor = models.ForeignKey(
        SportDoctor,
        on_delete=models.CASCADE,
        verbose_name="Medico",
        related_name="certificates"
    )

    class Meta:
        verbose_name = "Certificato Medico Sportivo"
        verbose_name_plural = "Certificati Medici Sportivi"
        ordering = ["-issued_date"]

    def __str__(self):
        return (f"Certificato {self.facility_id} - Emesso il {self.issued_date} "
                f"da {self.doctor}")
