from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from profiles.models.athletes import Athlete
from profiles.forms.athletes import AthleteForm


class AthleteListView(ListView):
    """View for listing all athletes."""
    model = Athlete
    template_name = "profiles/athletes_list.html"
    context_object_name = "athletes_list"


class AthleteDetailView(DetailView):
    """View for displaying a single athlete."""
    model = Athlete
    template_name = "profiles/athlete_detail.html"
    context_object_name = "athlete_detail"


class AthleteCreateView(CreateView):
    """View for creating a new athlete."""
    model = Athlete
    form_class = AthleteForm
    template_name = "profiles/athlete_form.html"
    success_url = reverse_lazy("athlete_list")


class AthleteUpdateView(UpdateView):
    """View for updating an athlete."""
    model = Athlete
    form_class = AthleteForm
    template_name = "profiles/athlete_form.html"

    def get_success_url(self):
        return reverse_lazy("athlete_detail", kwargs={"pk": self.object.pk})


class AthleteDeleteView(DeleteView):
    """View for deleting an athlete."""
    model = Athlete
    template_name = "profiles/athlete_confirm_delete.html"
    success_url = reverse_lazy("athlete_list")

