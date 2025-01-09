from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Fields to display in the admin panel
    list_display = ['username', 'is_superuser', 'is_staff', 'is_active']
    # Fields where you can search in the admin panel search bar
    search_fields = ['username', 'email']
    # Sidebar filters
    list_filter = ['is_superuser', 'is_staff', 'is_active']
    # Fields ordering
    ordering = ['-is_superuser', '-is_staff', '-is_active']

    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'bio')}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    # )


admin.site.register(CustomUser, CustomUserAdmin)
