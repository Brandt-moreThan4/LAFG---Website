from django import forms
from .models import Person



"""All these choices are used as the inputs for the django widgets in order to produce the radio fields"""

SEX_CHOICES = [('Male','Male') , ('Female','Female')]
ETHNICITY_CHOICES = [('White','White'),
                    ('African American/Black','African American/Black'),
                    ('Asian','Asian'),
                    ('Hispanic','Hispanic'),
                    ('Other','Other')]
POLITICAL_VIEW_CHOICES = [('Liberal','Liberal') , ('Moderate','Moderate'), ('Conservative','Conservative')]

MARITAL_STATUS_CHOICES = [('Single','Single'),
                          ('Married','Married'),
                          ('Divorced','Divorced'),
                          ('Widowed','Widowed'),
                          ('Separated','Separated')]
INCOME_CHOICES = [('Liberal','Liberal') , ('Moderate','Moderate'), ('Conservative','Conservative')]
WORKING_CHOICES = [('Yes','Yes') , ('No','No'), ('Student','Student'), ('Retired','Retired')]
EDUCATION_CHOICES = [('Some School','Some School'),
                     ('High School or GED','High School or GED'),
                     ('College Graduate','College Graduate'),
                     ('Post Graduate','Post Graduate')]
US_CITIZEN_CHOICES = [('Yes','Yes') , ('No','No')]
REGISTERED_VOTER_CHOICES = [('Yes','Yes') , ('No','No')]
RELIGIOUS_CHOICE = [('Yes','Yes') , ('No','No')]
PREVIOUS_FOCUS_GROUP_CHOICES = [('Yes','Yes') , ('No','No')]
PARTY_TO_LAW_SUIT_CHOICES = [('Yes','Yes') , ('No','No')]
FELONY_CHOICES = [('Yes','Yes') , ('No','No')]
LEGAL_BACKGROUND_CHOICES = [('Yes','Yes') , ('No','No')]
LOCATION_CHOICES = [('Baton Rouge','Baton Rouge'),
                    ('Metairie','Metairie'),
                    ('Shreveport','Shreveport'),
                    ('Lafayette','Lafayette'),
                    ('New Orleans','New Orleans'),]
SOURCES_CHOICES = [('Family/Friend','Family/Friend'),
                    ('Facebook','Facebook'),
                    ('Instagram','Instagram'),
                    ('Other','Other')]
        


class PersonForm(forms.ModelForm):
    """Sign_Up submission form"""
    #I should add some javascript for race field and occupation field to make an inut box if 'other' is selected
    class Meta:
        model = Person
        fields = '__all__'

        # All the widgets are needed to make some better html than Django's defaults.
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'first-name', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'last-name', 'placeholder':'Last Name'}),
            'email': forms.TextInput(attrs={'class':'email', 'placeholder':'email@domain.com' }),
            'phone': forms.TextInput(attrs={'type':'tel'}),
            'sex': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=SEX_CHOICES),
            'ethnicity': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=ETHNICITY_CHOICES),
            'political_view': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=POLITICAL_VIEW_CHOICES),
            'marital_status': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=MARITAL_STATUS_CHOICES),     
            #'children': forms.IntegerField(attrs={'min':0}),
            'income': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=ETHNICITY_CHOICES),
            'working': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=WORKING_CHOICES),
            'education': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=EDUCATION_CHOICES),
            'us_citizen': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=US_CITIZEN_CHOICES),
            'registered_voter': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=REGISTERED_VOTER_CHOICES),
            'religious': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=RELIGIOUS_CHOICE),
            'previous_focus_group': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=PREVIOUS_FOCUS_GROUP_CHOICES),
            'party_to_law_suit': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=PARTY_TO_LAW_SUIT_CHOICES),
            'felony': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=FELONY_CHOICES),
            'legal_background': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=LEGAL_BACKGROUND_CHOICES),
            'location': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=LOCATION_CHOICES),
            'source': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=SOURCES_CHOICES),
        }
