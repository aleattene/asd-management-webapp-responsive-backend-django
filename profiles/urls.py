from django.urls import path
from profiles.views.athletes import athlete_list, athlete_detail, athlete_create, athlete_update, athlete_delete

urlpatterns = [
    # Athletes
    path("athletes/", athlete_list, name="athletes_list"),
    path("athletes/<int:pk>/", athlete_detail, name="athlete_detail"),
    path("athletes/new/", athlete_create, name="athlete_create"),
    path("athletes/<int:pk>/edit/", athlete_update, name="athlete_update"),
    path("athletes/<int:pk>/delete/", athlete_delete, name="athlete_delete"),
]
