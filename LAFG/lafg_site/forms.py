from django import forms
from .models import Person



"""All these choices are used as the inputs for the django widgets in order to produce the radio fields"""
SEX_CHOICES = [('Male','Male') , ('Female','Female')]
ETHNICITY_CHOICES = [('White','White'),
                    ('African American/Black','African American/Black'),
                    ('Asian','Asian'),
                    ('Hispanic','Hispanic'),
                    ('African American/Black','African American/Black'),
                    ('Other','Other')]
POLITICAL_VIEW_CHOICES = [('Liberal','Liberal') , ('Moderate','Moderate'), ('Conservative','Conservative')]

]


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
            'sex': forms.RadioSelect(attrs={'class':'sexy'}, choices=SEX_CHOICES),
            'ethnicity': forms.RadioSelect(attrs={'class':'ethnicity'}, choices=ETHNICITY_CHOICES),
            'political_view': forms.RadioSelect(attrs={'class':'political-view'}, choices=POLITICAL_VIEW_CHOICES),
        }

    #ethnicity = models.CharField(max_length=50)
    #political_view = models.CharField(max_length=50)
    #marital_status = models.CharField(max_length=50)
    #children = models.IntegerField()
    #income = models.CharField(max_length=250)
    #working = models.CharField(max_length=3)
    #occupation = models.CharField(max_length=100)
    #us_citizen = models.CharField(max_length=3)
    #registered_voter = models.CharField(max_length=3)
    #religious = models.CharField(max_length=3)
    #previous_focus_group = models.CharField(max_length=3)
    #party_to_law_suit = models.CharField(max_length=3)
    #legal_background = models.CharField(max_length=3)
    #location = models.CharField(max_length=250)
    #source = models.CharField(max_length=250)