from django import forms
from documentation.models.sport_certificates import SportCertificate


class SportCertificateForm(forms.ModelForm):
    class Meta:
        model = SportCertificate
        fields = "__all__"
