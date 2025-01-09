from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Application name
    name = 'users'
    # Application verbose name (displayed in the admin panel)
    verbose_name = 'Gestione Utenti'

