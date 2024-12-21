from django.urls import path
from documentation.views.sport_certificates import (
    SportCertificateListView, SportCertificateDetailView, SportCertificateCreateView, SportCertificateUpdateView, SportCertificateDeleteView
)


urlpatterns = [
    # Sport Certificates
    path("sport_certificates/", SportCertificateListView.as_view(), name="sport_certificate_list"),
    path("sport_certificates/<int:pk>/", SportCertificateDetailView.as_view(), name="sport_certificate_detail"),
    path("sport_certificates/new/", SportCertificateCreateView.as_view(), name="sport_certificate_create"),
    path("sport_certificates/<int:pk>/edit/", SportCertificateUpdateView.as_view(), name="sport_certificate_update"),
    path("sport_certificates/<int:pk>/delete/", SportCertificateDeleteView.as_view(), name="sport_certificate_delete"),
    
]
