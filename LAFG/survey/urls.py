from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'survey'

urlpatterns = [
    path('test_case/<slug:survey_name>/', views.survey, name='survey'),
    ]

