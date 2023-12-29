from django.db import models
from django.conf import settings

# Create your models here.

class Test(models.Model):
    course_id = models.CharField(max_length=50, primary_key = True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Choice(models.Model):
    value = models.CharField(max_length=1)
    question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name = 'choices')
    choice = models.CharField(max_length = 50)
    is_correct= models.BooleanField(default = False)


class Question(models.Model):
    course = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.TextField(blank = False)


class Answer(models.Model):
    course = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name = 'answer')
    answer = models.CharField(max_length=5, blank = True)
    marks = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Result(models.Model):
    total = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Test, on_delete=models.CASCADE)