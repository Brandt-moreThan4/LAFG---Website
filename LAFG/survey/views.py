from django.shortcuts import render



print('http://127.0.0.1:8000/survey/test_case')


def test_case(request):
    """Renders home/ about page"""

    return render(request, 'survey/test_case.html')