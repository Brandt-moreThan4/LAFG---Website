from django.shortcuts import render
from django.contrib.auth.decorators import login_required


print('http://127.0.0.1:8000/survey/test_case')


@login_required
def test_case(request):
    """Renders home/ about page"""

    return render(request, 'survey/test_case.html')