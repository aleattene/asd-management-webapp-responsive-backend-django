from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import (
    LoginView as DjangoLoginView,
    LogoutView as DjangoLogoutView,
    PasswordChangeView as DjangoPasswordChangeView,
    PasswordChangeDoneView as DjangoPasswordChangeDoneView,
    PasswordResetView as DjangoPasswordResetView,
    PasswordResetDoneView as DjangoPasswordResetDoneView,
    PasswordResetConfirmView as DjangoPasswordResetConfirmView,
    PasswordResetCompleteView as DjangoPasswordResetCompleteView
)
from .forms import CustomUserCreationForm

from django.shortcuts import redirect
from django.contrib.auth import logout


# Signup
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')


# Login
class LoginView(DjangoLoginView):
    template_name = 'accounts/login.html'


# Logout
class LogoutView(DjangoLogoutView):
    template_name = 'accounts/logout.html'


# Password Change
class PasswordChangeView(DjangoPasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('password_change_done')


class PasswordChangeDoneView(DjangoPasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'


# Password Reset
class PasswordResetView(DjangoPasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')


class PasswordResetDoneView(DjangoPasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class PasswordResetConfirmView(DjangoPasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')


class PasswordResetCompleteView(DjangoPasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
