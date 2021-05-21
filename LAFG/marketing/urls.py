from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'marketing'

urlpatterns = [
    # path('contact/', views.contact, name='contact' ),
    path('', views.home, name='home' ),
    ]
