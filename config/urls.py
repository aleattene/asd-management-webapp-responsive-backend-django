"""
URL configuration for asd_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Homepage
    path('', include('home.urls')),
    # Admin Area
    path('admin/', admin.site.urls),
    # Templates
    path('products/', include('products.urls')),
    path('profiles/', include('profiles.urls')),
    path('documentation/', include('documentation.urls')),
    # APIs
    path('api/', include('products.api.urls'))
]


urlpatterns += [
    path('accounts/', include('accounts.urls')),
    # User Authentication
    path('accounts/', include('django.contrib.auth.urls')),
    # Login: /accounts/login/
    # Logout: /accounts/logout/
    # Password Change: /accounts/password_change/
    # Password Change Done: /accounts/password_change/done/
    # Password Reset: /accounts/password_reset/
    # Password Reset Done: /accounts/password_reset/done/
    # Password Reset Confirm: /accounts/reset/<uidb64>/<token>/
    # Password Reset Complete: /accounts/reset/done/

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
