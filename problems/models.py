from django.db import models

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