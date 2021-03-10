from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest, QueryDict
from django.core.paginator import Paginator
from django.urls import reverse

from .models import Survey
from .data import data_process as dp

print('http://127.0.0.1:8000/survey/test_case/Survey-1')




def survey(request: HttpRequest, survey_name):
    """Renders survey 1"""

    survey = get_object_or_404(Survey, survey_name=survey_name)

    if request.method == 'GET':
        return render(request, survey.get_template_path())
    elif request.method == 'POST':
        try:
            dp.process_form(survey, request.POST)
        except:
            return HttpResponseRedirect('survey/survey-submit-error/')
        else:
            success = True # Indicate that the survey was saved to csv
            survey_key = dp.generate_random_survey_key()
            return redirect('survey:survey_success', survey_key=survey_key)



def survey_success(request, survey_key):
    """Loads the survey success page which will appear after someone successfully completes the form"""

    return render(request, 'survey/survey_complete.html', context={'survey_key':survey_key})


def survey_fail(request):

    return render(request, 'survey/survey_submit_error.html')



    
