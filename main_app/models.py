from django.db import models

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField(max_length=250)
    sentence = models.TextField(max_length=250)
    