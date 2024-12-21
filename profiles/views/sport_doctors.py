from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from profiles.models.sport_doctors import SportDoctor
from profiles.forms.sport_doctors import SportDoctorForm


class SportDoctorListView(ListView):
    """View for listing all sport doctors."""
    model = SportDoctor
    template_name = "profiles/sport_doctor_list.html"
    context_object_name = "sport_doctor_list"


class SportDoctorDetailView(DetailView):
    """View for displaying a single sport doctor."""
    model = SportDoctor
    template_name = "profiles/sport_doctor_detail.html"
    context_object_name = "sport_doctor_detail"


class SportDoctorCreateView(CreateView):
    """View for creating a new sport doctor."""
    model = SportDoctor
    form_class = SportDoctorForm
    template_name = "profiles/sport_doctor_form.html"
    success_url = reverse_lazy("sport_doctor_list")


class SportDoctorUpdateView(UpdateView):
    """View for updating a sport doctor."""
    model = SportDoctor
    form_class = SportDoctorForm
    template_name = "profiles/sport_doctor_form.html"

    def get_success_url(self):
        return reverse_lazy("sport_doctor_detail", kwargs={"pk": self.object.pk})


class SportDoctorDeleteView(DeleteView):
    """View for deleting a sport doctor."""
    model = SportDoctor
    template_name = "profiles/sport_doctor_confirm_delete.html"
    success_url = reverse_lazy("sport_doctor_list")
