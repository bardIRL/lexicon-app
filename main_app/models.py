from django.db import models
from django.urls import reverse

PARTS_OF_SPEECH = (
    ('noun','noun'),
    ('verb','verb'),
    ('adjective','adjective'),
    ('adverb','adverb'),
)

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=100)
    part_of_speech = models.CharField(
        max_length=100,
        choices=PARTS_OF_SPEECH,
    )
    definition = models.CharField(max_length=250)
    etymology = models.CharField(max_length=250)
    sentence = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.word} ({self.id})'

class Synonym(models.Model):
    synonym = models.CharField(max_length=100)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.synonym} ({self.id})'

    
    