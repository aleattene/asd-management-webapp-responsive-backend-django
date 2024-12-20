from django import forms
from profiles.models.trainers import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"
