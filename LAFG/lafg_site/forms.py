from django import forms
from .models import Person, Place



"""All these choices are used as the inputs for the django widgets in order to produce the radio fields"""

SEX_CHOICES = [('Male','Male') , ('Female','Female')]

ETHNICITY_CHOICES = [('Asian','Asian'),
                    ('Black or African American','Black or African American'),
                    ('Hispanic or Latino','Hispanic or Latino'),
                    ('White','White'),
                    ('Native Hawaiian or Other Pacific Islander', 'Native Hawaiian or Other Pacific Islander'),
                    ('Other','Other')]

POLITICAL_VIEW_CHOICES = [('Liberal','Liberal') , ('Moderate','Moderate'), ('Conservative','Conservative')]

MARITAL_STATUS_CHOICES = [('Single','Single'),
                          ('Married','Married'),
                          ('Divorced','Divorced'),
                          ('Widowed','Widowed'),
                          ('Separated','Separated')]

INCOME_CHOICES = [('Less than $15,000','Less than $15,000'),
                  ('$15,000 - $30,000','$15,000 - $30,000'),
                  ('$31,000 - $60,000','$31,000 - $60,000'),
                  ('$61,000 - $90,000','$61,000 - $90,000'),
                  ('Over $90,000','Over $90,000')]

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


LOCATION_CHOICES = [('Harrison County','Harrison County, TX'),
                    ('Roane County','Roane County, TN'),
                    ('Knoxville','Knoxville, TN'),    
                    ('Baton Rouge','Baton Rouge, LA'),
                    ('Metairie','Metairie, LA'),
                    ('Shreveport','Shreveport, LA'),                
                    ('New Orleans','New Orleans, LA'),]


place_query = Place.objects.filter(display=True)
loc_labels = [place.city_label for place in place_query]
loc_values = [place.city_value for place in place_query]
LOCATION_CHOICES = list(zip(loc_values, loc_labels))
# print('done')

SOURCES_CHOICES = [('Family/Friend','Family/Friend'),
                    ('Facebook','Facebook'),
                    ('Instagram','Instagram'),
                    ('Other','Other')]
        

def get_location_choices():
    place_query = Place.objects.filter(display=True)
    loc_labels = [place.city_label for place in place_query]
    loc_values = [place.city_value for place in place_query]
    LOCATION_CHOICES = list(zip(loc_values, loc_labels))
    return LOCATION_CHOICES

class PersonForm(forms.ModelForm):
    """Sign_Up submission form"""

    # Must do the below line so that you can set required to false.
    occupation = forms.CharField(required=False, label = 'If you are working, what is your occupation?', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourceOther = forms.CharField(required=False, label = 'If other, please specify.', widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        # This function makes sure the rendered choices for location button are dynamic and based off the the 'Places' model.
        super().__init__(*args, **kwargs)
        locations= get_location_choices()
        self.fields["location"].widget.choices = locations

    
    class Meta:
        model = Person
        fields = '__all__'

        labels = {
            'children': ('How many children do you have?'),
            'income': ('What is your annual household income?'),
            'working': ('Are you working?'),
            'education': ('Highest level of education attained?'),
            'us_citizen': ('Are you a U.S Citizen?'),
            'registered_voter': ('Are you a registered voter?'),
            'religious': ('Religious?'),
            'previous_focus_group ':('Have you ever participated in a focus group about a legal issue?'),
            'party_to_law_suit': ('Have you ever been party to a lawsuit?'),
            'felony': ('Have you ever been convicted of a felony?'),
            'legal_background': ('Are you studying law or have you worked for a law firm?'),
            'location': ("Please indicate where you're located:"),
            'source': ('How did you hear about us?'),
        }


        
        # All the widgets are needed to make some better html than Django's defaults.
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'email@example.com' }),
            'phone': forms.TextInput(attrs={'class':'form-control', 'type':'tel', 'placeholder':'999-999-9999'}),
            'age': forms.NumberInput(attrs={'class':'form-control', 'min':0}),
            'sex': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=SEX_CHOICES),
            'ethnicity': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=ETHNICITY_CHOICES),
            'political_view': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=POLITICAL_VIEW_CHOICES),
            'marital_status': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=MARITAL_STATUS_CHOICES),                  
            'children': forms.NumberInput(attrs={'class':'form-control', 'min':0}),
            'income': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=INCOME_CHOICES),
            'working': forms.RadioSelect(attrs={'class':'ethnicity', 'onclick':'showHideOccupation()'}, choices=WORKING_CHOICES),
            'education': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=EDUCATION_CHOICES),
            'us_citizen': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=US_CITIZEN_CHOICES),
            'registered_voter': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=REGISTERED_VOTER_CHOICES),
            'religious': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=RELIGIOUS_CHOICE),
            'previous_focus_group': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=PREVIOUS_FOCUS_GROUP_CHOICES),
            'party_to_law_suit': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=PARTY_TO_LAW_SUIT_CHOICES),
            'felony': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=FELONY_CHOICES),
            'legal_background': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=LEGAL_BACKGROUND_CHOICES),
            'location': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=LOCATION_CHOICES),
            'source': forms.RadioSelect(attrs={'class':'ethnicity','onclick':'showHideSourceOther()'}, choices=SOURCES_CHOICES),
        }

        

    

