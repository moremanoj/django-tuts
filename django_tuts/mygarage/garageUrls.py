from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='garage-home'),
    path('about/', views.About, name='garage-about'),
    path('service/', views.Service, name='garage-service'),
    path('history/', views.History, name='garage-history'),
    path('login/', views.Login, name='garage-login'),
    path('register/', views.Register, name='garage-register'),
    path('admin/', views.AdminCalender, name='garage-admin'),
]
