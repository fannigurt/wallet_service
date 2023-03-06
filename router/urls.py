"""wallet_service URL Configuration
https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.urls import path

from wallet_app.api.default import default_handler

urlpatterns = [
    path("", default_handler)
]
