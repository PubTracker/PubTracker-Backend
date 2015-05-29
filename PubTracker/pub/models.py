from django.db import models
import json


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class RssNewsItem(models.Model):
    def __init__(self, title, summary):
        self.title = title
        self.summary = summary