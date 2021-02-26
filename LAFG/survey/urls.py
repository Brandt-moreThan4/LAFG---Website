from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'survey'

urlpatterns = [
    path('test_case/', views.test_case, name='test_case'),
    ]
