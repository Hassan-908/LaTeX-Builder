from django.urls import path
from .views import render_tex

urlpatterns = [
    path("", render_tex),
]
