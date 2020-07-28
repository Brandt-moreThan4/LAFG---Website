from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PersonForm
from django.contrib.auth.decorators import login_required


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

    # Below variable is used to decide thank you message should be shown or if the from should be shown.
    form_submitted = False

     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            form_submitted = True 

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonForm()

    return render(request, 'lafg_site/sign_up.html', {'form': form, 'form_submitted': form_submitted})


@login_required
def data(request):
    """This is the page they will be re-directed to after submitting a sign-up form"""

    return render(request, 'lafg_site/data.html')