from django.urls import path
from profiles.views.athletes import (
    AthleteListView, AthleteDetailView, AthleteCreateView, AthleteUpdateView, AthleteDeleteView
)
from profiles.views.trainers import (
    TrainerListView, TrainerDetailView, TrainerCreateView, TrainerUpdateView, TrainerDeleteView
)

urlpatterns = [
    # Athletes
    path("athletes/", AthleteListView.as_view(), name="athletes_list"),
    path("athletes/<int:pk>/", AthleteDetailView.as_view(), name="athlete_detail"),
    path("athletes/new/", AthleteCreateView.as_view(), name="athlete_create"),
    path("athletes/<int:pk>/edit/", AthleteUpdateView.as_view(), name="athlete_update"),
    path("athletes/<int:pk>/delete/", AthleteDeleteView.as_view(), name="athlete_delete"),

    # Trainers
    path("trainers/", TrainerListView.as_view(), name="trainers_list"),
    path("trainers/<int:pk>/", TrainerDetailView.as_view(), name="trainer_detail"),
    path("trainers/new/", TrainerCreateView.as_view(), name="trainer_create"),
    path("trainers/<int:pk>/edit/", TrainerUpdateView.as_view(), name="trainer_update"),
    path("trainers/<int:pk>/delete/", TrainerDeleteView.as_view(), name="trainer_delete"),
]
