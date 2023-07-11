from django.db import models

# Create your models here.
class questions(models.Model):
    statement=models.TextField()
    name=models.TextField()
    code= models.TextField()
    difficulty= models.CharField(max_length=100)