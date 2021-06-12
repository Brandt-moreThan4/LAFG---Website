from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'lafg_site'

urlpatterns = [
    path('contact/', views.contact, name='contact' ),
    path('services/', views.services, name='services' ),
    path('sign_up/', views.sign_up, name='sign_up' ),
    path('sign_up_success/', views.sign_up_success, name='sign_up_success' ),
    path('data/', views.data, name='data' ),
    path('faqs/', views.faqs, name='faqs' ),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.home, name='home' ),
    ]
