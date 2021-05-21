

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('lafg_site.urls', namespace='lafg_site')),
    path('survey/', include('survey.urls', namespace='survey')),
    path('manage/', admin.site.urls),
    path('lawyers/', include('marketing.urls', namespace='marketing'))
]
