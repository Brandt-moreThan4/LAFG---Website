from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest
from django.core.paginator import Paginator

from .models import Survey


print('http://127.0.0.1:8000/survey/test_case/Survey-1')




def survey(request: HttpRequest, survey_name):
    """Renders survey 1"""

    survey = get_object_or_404(Survey, survey_name=survey_name)
    if request.method == 'GET':
        return render(request, survey.get_template_path())
    elif request.method == 'POST':
        print('OMG we are in the post')
        data = request.POST

        # After doing everything send them to finish page
        HttpResponseRedirect('survey/survey_complete.html') 

        return render(request, survey.get_template_path())



