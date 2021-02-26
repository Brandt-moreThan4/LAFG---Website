from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import datetime

from .data_tools import data_export
from . models import Person
from .forms import PersonForm

print('http://127.0.0.1:8000/sign_up')

def home(request):
    """Renders home/ about page"""

    return render(request, 'lafg_site/index.html')


def contact(request):
    """Renders the conduct page"""

    return render(request, 'lafg_site/contact.html')


def conduct(request):
    """Renders the conduct a focus group about page"""

    return render(request, 'lafg_site/conduct.html')


def sign_up(request):
    """Renders the sign-up form"""

     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            form_submitted = True 
            return HttpResponseRedirect('/sign_up_success/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonForm()

    return render(request, 'lafg_site/sign_up.html', {'form': form})


def sign_up_success(request):
    """Renders the sign-up success template"""

    return render(request, 'lafg_site/sign_up_success.html')


@login_required
def data(request):
    """This is the page to export the participant list as a csv"""

    if request.method == 'POST':
        button_value = request.POST.get('data_export')
        if button_value == 'participant_export':

            # File name arguement for response object must be surrounded by quotes I think
            file_name = '"' + datetime.datetime.today().strftime('%Y-%m-%d') + '--participants.csv' + '"'
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=' + file_name
            data_export.export_db(Person, response) # Write the content to the response object

            return response


    return render(request, 'lafg_site/data.html')
