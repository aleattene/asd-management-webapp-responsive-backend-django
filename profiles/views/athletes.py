from django.shortcuts import render, get_object_or_404, redirect
from profiles.models.athletes import Athlete
from profiles.forms.athletes import AthleteForm


def athlete_list(request):
    """View function for listing all athletes."""
    athletes = Athlete.objects.all()
    return render(request, "profiles/athletes_list.html", {"athletes_list": athletes})


def athlete_detail(request, pk):
    """View function for showing a single athlete."""
    athlete = get_object_or_404(Athlete, pk=pk)
    return render(request, "athletes/athlete_detail.html", {"athlete_detail": athlete})


def athlete_create(request):
    """View function for creating a new athlete."""
    if request.method == "POST":
        form = AthleteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("athlete_list")
    else:
        form = AthleteForm()
    return render(request, "athletes/athlete_form.html", {"form": form})


def athlete_update(request, pk):
    """View function for updating an athlete."""
    athlete = get_object_or_404(Athlete, pk=pk)
    if request.method == "POST":
        form = AthleteForm(request.POST, instance=athlete)
        if form.is_valid():
            form.save()
            return redirect("athlete_detail", pk=athlete.pk)
    else:
        form = AthleteForm(instance=athlete)
    return render(request, "athletes/athlete_form.html", {"form": form})


def athlete_delete(request, pk):
    """View function for deleting an athlete."""
    athlete = get_object_or_404(Athlete, pk=pk)
    if request.method == "POST":
        athlete.delete()
        return redirect("athlete_list")
    return render(request, "athletes/athlete_confirm_delete.html", {"athlete": athlete})
