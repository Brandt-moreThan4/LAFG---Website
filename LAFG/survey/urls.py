from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'survey'

urlpatterns = [
    path('test_case/<slug:survey_name>/', views.survey, name='survey'),
    # I really feel like I should just be able to pass the survey key to the view somehow without it being in the url?
    path('survey-success/<str:survey_key>/', views.survey_success, name='survey_success'), 
    path('survey-submit-error/', views.survey_fail, name='survey_fail')
    ]

