from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest, QueryDict, HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse
import datetime

from .models import Survey
from .data import data_process as dp

print('http://127.0.0.1:8000/survey/surveys/Survey-1')
print('http://127.0.0.1:8000/survey/survey-export/')




def survey(request: HttpRequest, survey_name):
    """Renders surveys based on survey name provided in url"""

    survey = get_object_or_404(Survey, survey_name=survey_name, active=True)
    
    if request.method == 'GET':
        return render(request, survey.get_template_path())
    elif request.method == 'POST':
        try:
            # print(four)
            survey_key = dp.process_form(survey, request.POST)# Feels weird. Wish I could do the survey key separately from saving it.

        except:
            response = redirect('survey:survey_fail')
            return response
        else:
            return redirect('survey:survey_success', survey_key=survey_key)



def survey_success(request, survey_key):
    """Loads the survey success page which will appear after someone successfully completes the form"""

    return render(request, 'survey/survey_complete.html', context={'survey_key':survey_key})


def survey_fail(request):

    return render(request, 'survey/survey_submit_error.html')

def survey_help(request):
    """"""
    return render(request, 'survey/help.html')



def survey_export(request):
    """ """
    # Should probably just make this so that I can return the csv directly include it as an href link?
    if request.method == 'POST':
        button_value = request.POST.get('data_export')
        file_name = button_value + '.csv'
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=' + file_name
        dp.write_csv_to_response(button_value, response)
        return response

    return render(request, 'survey/survey_export.html')
    
