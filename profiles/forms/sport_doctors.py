from django import forms
from profiles.models.sport_doctors import SportDoctor


class SportDoctorForm(forms.ModelForm):
    class Meta:
        model = SportDoctor
        fields = "__all__"
