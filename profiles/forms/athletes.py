from django import forms
from profiles.models.athletes import Athlete


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = "__all__"
