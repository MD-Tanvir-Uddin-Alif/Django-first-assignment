from django.urls import path
from .import views

urlpatterns = [
    path('show-Items/', views.showItems,name='ShowItems')
]