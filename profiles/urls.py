from django.urls import path
from profiles.views.athletes import (
    AthleteListView, AthleteDetailView, AthleteCreateView, AthleteUpdateView, AthleteDeleteView
)
from profiles.views.trainers import (
    TrainerListView, TrainerDetailView, TrainerCreateView, TrainerUpdateView, TrainerDeleteView
)

from profiles.views.sport_doctors import (
    SportDoctorListView, SportDoctorDetailView, SportDoctorCreateView, SportDoctorUpdateView, SportDoctorDeleteView
)

urlpatterns = [
    # Athletes
    path("athletes/", AthleteListView.as_view(), name="athlete_list"),
    path("athletes/<int:pk>/", AthleteDetailView.as_view(), name="athlete_detail"),
    path("athletes/new/", AthleteCreateView.as_view(), name="athlete_create"),
    path("athletes/<int:pk>/edit/", AthleteUpdateView.as_view(), name="athlete_update"),
    path("athletes/<int:pk>/delete/", AthleteDeleteView.as_view(), name="athlete_delete"),

    # Trainers
    path("trainers/", TrainerListView.as_view(), name="trainer_list"),
    path("trainers/<int:pk>/", TrainerDetailView.as_view(), name="trainer_detail"),
    path("trainers/new/", TrainerCreateView.as_view(), name="trainer_create"),
    path("trainers/<int:pk>/edit/", TrainerUpdateView.as_view(), name="trainer_update"),
    path("trainers/<int:pk>/delete/", TrainerDeleteView.as_view(), name="trainer_delete"),

    # Sport Doctors
    path("sport_doctors/", SportDoctorListView.as_view(), name="sport_doctor_list"),
    path("sport_doctors/<int:pk>/", SportDoctorDetailView.as_view(), name="sport_doctor_detail"),
    path("sport_doctors/new/", SportDoctorCreateView.as_view(), name="sport_doctor_create"),
    path("sport_doctors/<int:pk>/edit/", SportDoctorUpdateView.as_view(), name="sport_doctor_update"),
    path("sport_doctors/<int:pk>/delete/", SportDoctorDeleteView.as_view(), name="sport_doctor_delete"),
]
