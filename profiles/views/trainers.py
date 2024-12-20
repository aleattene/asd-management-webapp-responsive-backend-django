from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from profiles.models.trainers import Trainer
from profiles.forms.trainers import TrainerForm


class TrainerListView(ListView):
    """View for listing all trainers."""
    model = Trainer
    template_name = "profiles/trainers_list.html"
    context_object_name = "trainers_list"


class TrainerDetailView(DetailView):
    """View for displaying a single trainer."""
    model = Trainer
    template_name = "profiles/trainer_detail.html"
    context_object_name = "trainer_detail"


class TrainerCreateView(CreateView):
    """View for creating a new trainer."""
    model = Trainer
    form_class = TrainerForm
    template_name = "profiles/trainer_form.html"
    success_url = reverse_lazy("trainers_list")


class TrainerUpdateView(UpdateView):
    """View for updating an trainer."""
    model = Trainer
    form_class = TrainerForm
    template_name = "profiles/trainer_form.html"

    def get_success_url(self):
        return reverse_lazy("trainer_detail", kwargs={"pk": self.object.pk})


class TrainerDeleteView(DeleteView):
    """View for deleting an athlete."""
    model = Trainer
    template_name = "profiles/trainer_confirm_delete.html"
    success_url = reverse_lazy("trainers_list")
