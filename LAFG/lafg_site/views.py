from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PersonForm


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
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonForm()



    return render(request, 'lafg_site/sign_up.html', {'form': form}) 


def sign_up2(request):

    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
    # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonForm()


    return render(request, 'lafg_site/sign-up2.html', {'form': form}) 