from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


class Survey(models.Model):
    """Each row will contain some high level data for a survey"""

    survey_name = models.SlugField(max_length=300, unique=True)
    active = models.BooleanField(default=True)


    def get_template_path(self):
        return f'survey/surveys/{self.survey_name}.html'

    def get_csv_path(self):
        pass

    def __str__(self):
        return self.survey_name