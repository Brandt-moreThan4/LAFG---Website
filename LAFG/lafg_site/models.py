from django.db import models



class Person(models.Model):
    """Class to model a potential participant"""
    
    time_stamp = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    ethnicity = models.CharField(max_length=50)
    political_view = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=50)
    children = models.IntegerField()
    income = models.CharField(max_length=250)
    working = models.CharField(max_length=3)
    occupation = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    us_citizen = models.CharField(max_length=3)
    registered_voter = models.CharField(max_length=3)
    religious = models.CharField(max_length=3)
    previous_focus_group = models.CharField(max_length=3)
    party_to_law_suit = models.CharField(max_length=3)
    felony = models.CharField(max_length=3)
    legal_background = models.CharField(max_length=3)
    location = models.CharField(max_length=250)
    source = models.CharField(max_length=250)

