from django.db import models

# Create your models here.


class Question(models.Model):
    theme = models.CharField(default='', max_length=3)
    question = models.TextField()
    ansA = models.TextField(default='')
    ansB = models.TextField(default='')
    ansC = models.TextField(default='')
    ansD = models.TextField(default='')
    ansE = models.TextField(default='')
    answered = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)
