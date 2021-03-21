from django.db import models


class Survey(models.Model):
    """Each row will contain some high level data for a survey"""

    survey_name = models.SlugField(max_length=300, unique=True)
    active = models.BooleanField(default=True)
    url_slug = models.SlugField(max_length=300, unique=True)
    column_headers = models.TextField(default='lol')




    def get_template_path(self):
        return f'survey/surveys/{self.survey_name}.html'

    def get_csv_path(self):
        return f'LAFG/survey/data/survey_exports/{self.survey_name}.csv'

    def __str__(self):
        return self.survey_name


class Survey_Key(models.Model):
    key = models.CharField(max_length=300, unique = True)

    def __str__(self):
        return self.key
    

# Should change the name..
class Survey_Record(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.survey) +': ' + str(self.timestamp)