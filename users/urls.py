from django.urls import path
from users.views import UserProfileView  # UserDashboardView

app_name = 'users'

urlpatterns = [
    # path('dashboard/', UserDashboardView.as_view(), name='dashboard'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
