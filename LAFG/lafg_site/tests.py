"""
Run with python ./manage.py test lafg_site
"""

import django
from django.test import TestCase
from . models import Person


class PersonTest(TestCase):
    """Test for if creating a person works."""

    def test_create_valid_person(self):
        new_person = Person()
        new_person.first_name = "Test_Clarance"
        new_person.last_name = 'Test_Leblanc'
        new_person.email = 'brandtgreen97@gmail.com'
        new_person.phone = '2259074265'
        new_person.age = 22
        new_person.sex = 'Male'
        new_person.ethnicity = 'Black'
        new_person.political_view = 'Liberal'
        new_person.marital_status = 'Single'
        new_person.children = 2
        new_person.income = '$15,000 - $30,000'
        new_person.working = 'Yes'
        new_person.occupation = 'Butcher'
        new_person.education = 'College Graduate'
        new_person.us_citizen = 'Yes'
        new_person.registered_voter = 'Yes'
        new_person.religious = 'Yes' 
        new_person.previous_focus_group = 'No'
        new_person.party_to_law_suit = 'No'
        new_person.felony = 'No'
        new_person.legal_background = 'Yes'
        new_person.location = 'Baton Rouge'
        new_person.source = 'Facebook'
        new_person.save()

        self.assertEqual(True,True)
