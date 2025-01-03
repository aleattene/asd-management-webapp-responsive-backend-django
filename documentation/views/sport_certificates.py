from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from documentation.models.sport_certificates import SportCertificate
from documentation.forms.sport_certificates import SportCertificateForm


class SportCertificateListView(ListView):
    """View for listing all sport certificates."""
    model = SportCertificate
    template_name = "documentation/sport_certificate_list.html"
    context_object_name = "sport_certificate_list"


class SportCertificateDetailView(DetailView):
    """View for displaying a single sport certificate."""
    model = SportCertificate
    template_name = "documentation/sport_certificate_detail.html"
    context_object_name = "sport_certificate_detail"


class SportCertificateCreateView(CreateView):
    """View for creating a new sport certificate."""
    model = SportCertificate
    form_class = SportCertificateForm
    template_name = "documentation/sport_certificate_form.html"
    # Redirect to the list view after creation (status code 302)
    success_url = reverse_lazy("sport_certificate_list")


class SportCertificateUpdateView(UpdateView):
    """View for updating a sport certificate."""
    model = SportCertificate
    form_class = SportCertificateForm
    template_name = "documentation/sport_certificate_form.html"

    # Override the get_success_url method to redirect (302) to the detail view after updating
    def get_success_url(self):
        return reverse_lazy("sport_certificate_detail", kwargs={"pk": self.object.pk})


class SportCertificateDeleteView(DeleteView):
    """View for deleting a sport certificate."""
    model = SportCertificate
    template_name = "documentation/sport_certificate_confirm_delete.html"
    # Redirect to the list view after deletion (status code 302)
    success_url = reverse_lazy("sport_certificate_list")
