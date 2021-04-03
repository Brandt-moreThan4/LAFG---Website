from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest, QueryDict, HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse
import datetime
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Survey, Survey_Key
from .data import data_process as dp
from lafg_site.data_tools.data_export import export_db


# print('http://127.0.0.1:8000/survey/surveys/Survey-401A')
print('http://127.0.0.1:8000/survey/surveys/300')
print('http://127.0.0.1:8000/survey/survey-export/')




def survey(request: HttpRequest, survey_url):
    """Renders surveys based on survey name provided in url"""

    survey = get_object_or_404(Survey, url_slug=survey_url, active=True)
    
    if request.method == 'POST':
        """Captcha Stuff"""

        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        if result['success']:
            try:
                survey_key = dp.process_form(survey, request.POST) # Feels weird. Wish I could do the survey key separately from saving it.
            except:
                response = redirect('survey:survey_fail')
                return response
            else:
                return redirect('survey:survey_success', survey_key=survey_key)
    return render(request, survey.get_template_path())




def survey_success(request, survey_key):
    """Loads the survey success page which will appear after someone successfully completes the form"""

    return render(request, 'survey/survey_complete.html', context={'survey_key':survey_key})


def survey_fail(request):

    return render(request, 'survey/survey_submit_error.html')

def survey_help(request):
    """ Not actually using this."""
    return render(request, 'survey/help.html')


@login_required
def survey_export(request):
    """ """
    # Should probably just make this so that I can return the csv directly include it as an href link?
    if request.method == 'POST':
        survey_name = request.POST.get('data_export') 

        file_name = survey_name + '.csv'
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=' + file_name

        dp.write_records_to_response(survey_name, response)
        return response
    else:
        surveys = Survey.objects.all()
        

    return render(request, 'survey/survey_export.html',context={'surveys': surveys})
    
