from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import datetime


print('http://127.0.0.1:8000/lawyers/')

def home(request:HttpRequest):
    """Renders home page"""
    
    return render(request, 'marketing/home.html')
