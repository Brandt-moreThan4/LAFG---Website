from django.urls import path
from . import views

app_name = 'lafg_site'

urlpatterns = [
    path('', views.home, name='home' ),
    path('contact', views.contact, name='contact' ),
    path('conduct', views.conduct, name='conduct' ),
    path('sign_up', views.sign_up, name='sign_up' ),
    ]
