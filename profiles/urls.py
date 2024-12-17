from django.urls import path
from profiles.views.athletes import (
    AthleteListView, AthleteDetailView, AthleteCreateView, AthleteUpdateView, AthleteDeleteView
)

urlpatterns = [
    # Athletes
    path("athletes/", AthleteListView.as_view(), name="athletes_list"),
    path("athletes/<int:pk>/", AthleteDetailView.as_view(), name="athlete_detail"),
    path("athletes/new/", AthleteCreateView.as_view(), name="athlete_create"),
    path("athletes/<int:pk>/edit/", AthleteUpdateView.as_view(), name="athlete_update"),
    path("athletes/<int:pk>/delete/", AthleteDeleteView.as_view(), name="athlete_delete"),
]
