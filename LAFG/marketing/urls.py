from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'marketing'

urlpatterns = [
    path('contact/', views.contact, name='contact' ),
    path('faqs/', views.faqs, name='faqs' ),
    path('focus-groups/', views.focus_groups, name='focus_groups' ),
    path('demonstratives/', views.demonstratives, name='demonstratives'),
    path('surveys/', views.surveys, name='surveys' ),
    path('', views.home, name='home' ),
    ]
