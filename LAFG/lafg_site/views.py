from django.shortcuts import render


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

    return render(request, 'lafg_site/sign_up.html') 
