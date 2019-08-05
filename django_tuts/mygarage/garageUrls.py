from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='garage-home'),
    path('about/', views.About, name='garage-about'),
]
