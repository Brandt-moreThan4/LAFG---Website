from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


print('http://127.0.0.1:8000/survey/test_case/')



# def test_case(request, page_num):
#     """Renders home/ about page"""

#     if page_num <1:
#         page_num = 1
#     elif page_num > 2:
#         page_num = 2


#     template_path = 'survey/test_case' + str(page_num) + '.html'

#     return render(request, template_path)


def test_case(request):
    """Renders survey 1"""

    return render(request, 'survey/surveys/survey_1.html')



