from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import DetailView
from . import views

urlpatterns = [
    path('', views.Home, name='garage-home'),
    path('about/', views.About, name='garage-about'),
    path('service/', views.Service, name='garage-service'),
    path('history/<int:pk>', views.ServiceDetailView.as_view(), name='garage-history-details'),
    path('history/', views.History, name='garage-history'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='garage-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home.html'), name='garage-logout'),
    path('register/', views.Register, name='garage-register'),
    path('admin/', views.AdminCalender, name='garage-admin'),
]
