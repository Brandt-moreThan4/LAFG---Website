from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import datetime

# from . models import Person, Place, State, Faq
# from ..lafg_site.models import Faq
from lafg_site.models import Faq

print('http://127.0.0.1:8000/lawyers/')

def home(request:HttpRequest):
    """Renders home page"""
    
    return render(request, 'marketing/home.html')


def contact(request:HttpRequest):
    """Renders contact page"""
    
    return render(request, 'marketing/contact.html')


def faqs(request:HttpRequest):
    """Renders FAQ's page"""
    faqs = Faq.objects.all()

    return render(request, 'marketing/FAQs.html', context={'faqs': faqs})


def focus_groups(request:HttpRequest):
    """Renders focus gorups page"""

    return render(request, 'marketing/focus_groups.html')
    
def surveys(request:HttpRequest):
    """Renders focus gorups page"""

    return render(request, 'marketing/surveys.html')

def demonstratives(request:HttpRequest):
    """Renders focus gorups page"""

    return render(request, 'marketing/demonstratives.html')

def timeline(request:HttpRequest):
    """Renders timeline page"""

    return render(request, 'marketing/timeline.html')