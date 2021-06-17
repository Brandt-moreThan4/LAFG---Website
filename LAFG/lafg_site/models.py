from django.db import models



class State(models.Model):
    """Bet"""
    name = models.CharField(max_length=200)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    """Class to model a city"""

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city_value = models.CharField(max_length=200)
    city_label = models.CharField(max_length=200)
    display = models.BooleanField(default=True)

    # class Meta:
    def __str__(self):
        return self.city_label

class Faq(models.Model):
    """table used to hold faq questions and their answers"""
    question = models.TextField()
    answer = models.TextField()
    
    def __str__(self):
        return self.question



class Person(models.Model):
    """Class to model a potential participant"""
    
    time_stamp = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    zip = models.CharField(max_length=5)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    ethnicity = models.CharField(max_length=50)
    political_view = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=50)
    children = models.IntegerField()
    income = models.CharField(max_length=250)
    working = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    us_citizen = models.CharField(max_length=3)
    registered_voter = models.CharField(max_length=3)
    religious = models.CharField(max_length=3)
    previous_focus_group = models.CharField(max_length=3)
    party_to_law_suit = models.CharField(max_length=3)
    felony = models.CharField(max_length=3)
    legal_background = models.CharField(max_length=3)
    # location = models.CharField(max_length=250)
    source = models.CharField(max_length=250)
    sourceOther = models.CharField(max_length=250)

    class Meta:
        # abstract = True
        ordering = ('-time_stamp',)

