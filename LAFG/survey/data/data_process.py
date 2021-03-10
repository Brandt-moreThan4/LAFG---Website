import csv
from pathlib import Path
import string
import random
from django.http import HttpResponseRedirect, HttpRequest, QueryDict

from ..models import Survey


SURVEY_KEY_PATH: Path = Path(__file__).parent / 'survey_keys.csv'


def process_form(survey:Survey, query_dict: QueryDict):
    """Send in a Survey object along with a query dict, and this function will save the inputs from the query dict to a 
    new row in the survey's csv"""
    data_dict = dict(query_dict) # Necessary because there is some weirdness in accessing Query Dict
    # form_questions = list(data_dict.keys()) # Don't really need this?
    form_answers = list(data_dict.values())
    # Below logic converts the answers from their natural state -list objects- strings. 
    form_answers = [';'.join(answer) for answer in form_answers]
    save_form_to_csv(survey=survey, form_answers=form_answers)


def save_form_to_csv(survey:Survey, form_answers: list):
    """Appends the form responses to the survey csv path."""

    survey_csv_path = Path(survey.get_csv_path())

    with survey_csv_path.open('a',  newline='') as f:
        writer = csv.writer(f)
        writer.writerow(form_answers)


def generate_random_survey_key():
    """Generate a unique survey key composed of 6 characters that can be either numbers or digits."""
    #Should make some unit tests for these!
    key = get_new_key()
    while not key_is_valid(key):
        key = get_new_key()
    return key

def get_new_key():
    """Generate a unique survey key composed of 6 characters that can be either numbers or digits."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def key_is_valid(key: str) -> bool:
    """Returns true if the survey key is unique"""

    with SURVEY_KEY_PATH.open() as f:
        reader = csv.reader(f, delimiter=',')
        all_keys = []
        for row in reader:
            for col in row:
                all_keys.append(col)

        if key in all_keys:
            return False
        else:
            return True



def write_to_response(data, response):
    """Takes an interable of iterables like a list of lists and writes it to the response object as a csv?"""

    writer = csv.writer(response)
    writer.writerows(data)