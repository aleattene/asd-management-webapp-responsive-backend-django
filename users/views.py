from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# class UserDashboardView(LoginRequiredMixin, TemplateView):
#     template_name = 'users/dashboard.html'
#     # Redirect if not authenticated
#     login_url = '/accounts/login/'


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
    # Redirect if not authenticated
    login_url = '/accounts/login/'
