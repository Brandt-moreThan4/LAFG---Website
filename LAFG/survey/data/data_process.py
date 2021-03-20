"""I should change it so that all survey's save to the same file? Might not work unless they all have the same questions. """

import csv
from pathlib import Path
import string
import random
from django.http import HttpResponseRedirect, HttpRequest, QueryDict, HttpResponse
import datetime
import json

from ..models import Survey, Survey_Key, Survey_Record


SURVEY_KEY_PATH: Path = Path(__file__).parent / 'survey_keys.csv'


def process_form(survey:Survey, query_dict: QueryDict) -> str:
    """Send in a Survey object along with a query dict, and this function will save the inputs from the query dict to a 
    new row in the survey's csv. Returns a unique survey key"""
    data_dict = dict(query_dict) # Necessary because there is some weirdness in accessing Query Dict

    form_answers = list(data_dict.values())
    form_answers = [';'.join(answer) for answer in form_answers]  # Converts the answers from their natural state -list objects- strings. 

    survey_key = generate_random_survey_key()
    form_answers.insert(0, survey_key) # put survey key in the first column of the csv row
    form_answers.insert(0, datetime.datetime.now()) # Add time stamp

    create_new_survey_record(survey, form_answers)    
    # save_form_data_to_csv(survey=survey, form_answers=form_answers)

    return survey_key


def create_new_survey_record(survey:Survey, form_answers: list):
    survey_record = Survey_Record()
    survey_record.survey = survey
    json_form_answers = json.dumps(form_answers, default=str) # default is needed because datetime object isn't serailizable
    survey_record.response = json_form_answers
    survey_record.save()



def generate_random_survey_key() -> str:
    """Generate a unique survey key composed of 6 characters that can be either numbers or digits."""
    #Should make some unit tests for these!
    key = get_new_key()
    while not key_is_valid(key):
        key = get_new_key()
    
    # If the key is unique then write it to the csv file and return it.
    new_key = Survey_Key(key=key)
    new_key.save()
    return key


def get_new_key() -> str:
    """Generate a unique survey key composed of 6 characters that can be either numbers or digits."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


def key_is_valid(key: str) -> bool:
    """Returns true if the survey key is unique"""
    all_keys = [survey_key.key for survey_key in Survey_Key.objects.all()]
    if key in all_keys:
        return False
    else:
        return True




def write_records_to_response(button_value: str, response: HttpResponse):
    records = Survey_Record.objects.all().filter(survey__survey_name = button_value)
    record_responses = [record.response for record in records]
    records = [json.loads(record) for record in record_responses]
    csv.writer(response).writerows(records)
    print('lol')


# def save_form_data_to_csv(survey:Survey, form_answers: list):
#     """Appends the form responses to the survey csv path."""

#     # Really don't know why the below doesn't work
#     # survey_csv_path = Path(survey.get_csv_path())
#     survey_csv_path = Path(__file__).parent / 'survey_exports' / ( survey.survey_name +'.csv') 

#     with survey_csv_path.open('a',  newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(form_answers)


# def write_csv_to_response(survey_name, response):
#     """Takes an interable of iterables like a list of lists and writes it to the response object as a csv?"""
#     survey_csv_path = Path(__file__).parent / 'survey_exports' / ( survey_name +'.csv') 
#     survey_rows = load_csv(survey_csv_path) 
#     writer = csv.writer(response).writerows(survey_rows)
    


# def load_csv(file_path: Path):
    
#     with file_path.open('r') as f:
#         reader = csv.reader(f, delimiter = ',')
#         rows = list(reader)
#     return rows