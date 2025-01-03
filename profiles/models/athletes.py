from django.db import models


class Athlete(models.Model):
    """Model representing an athlete."""
    first_name = models.CharField(max_length=100, verbose_name="Nome")
    last_name = models.CharField(max_length=100, verbose_name="Cognome")
    date_of_birth = models.DateField(verbose_name="Data di Nascita")
    place_of_birth = models.CharField(max_length=150, verbose_name="Luogo di Nascita")
    fiscal_code = models.CharField(max_length=16, unique=True, verbose_name="Codice Fiscale")
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        verbose_name="Categoria",
        related_name="athletes"
    )

    trainer = models.ForeignKey(
        "Trainer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Trainer",
        related_name="athletes"
    )

    class Meta:
        verbose_name = "Atleta"
        verbose_name_plural = "Atleti"
        # ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.fiscal_code})"

    def __repr__(self):
        return (f"Athlete(first_name={self.first_name}, last_name={self.last_name}, "
                f"date_of_birth={self.date_of_birth}, fiscal_code={self.fiscal_code})")


class Category(models.Model):
    code = models.CharField(max_length=4, unique=True)
    description = models.CharField(max_length=50)
    age_range = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"
        # ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name}"

    def __repr__(self):
        return f"Category(code={self.code}, name={self.name}, age_range={self.age_range})"
