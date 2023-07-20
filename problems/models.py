from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.
class questions(models.Model):
    statement=models.TextField()
    name=models.TextField()
    code= models.TextField()
    difficulty= models.CharField(max_length=100)

class testcases(models.Model):
    question=models.ForeignKey(questions,on_delete=models.CASCADE)
    input=models.TextField()
    expected_output=models.TextField()

class totsubmission(models.Model):
    user=models.CharField(max_length=200)
    problem=models.CharField(max_length=500)
    verdict=models.CharField(max_length=100)
    time_of_submission=models.TimeField()
    language=models.CharField(max_length=20)
    date_of_submission=models.DateField()