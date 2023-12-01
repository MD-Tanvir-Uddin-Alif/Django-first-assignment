from django.urls import path
from .import views

urlpatterns = [
    path('About-Us', views.about, name="About"),
]