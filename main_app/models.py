from django.db import models
from django.urls import reverse

PARTS_OF_SPEECH = (
    ('noun','noun'),
    ('verb','verb'),
    ('adjective','adjective'),
    ('adverb','adverb'),
)

CONNOTATIONS = (
    ('positive', 'positive'),
    ('negative', 'negative'),
    ('neutral', 'neutral')
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
    connotation = models.CharField(
        max_length=100,
        choices=CONNOTATIONS,
        )
    sentence = models.TextField(max_length=250)

    def __str__(self):
        return self.word

class NearbyWord(models.Model):
    nearby_word = models.CharField(max_length=100)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    def __str__(self):
        return self.nearby_word

class Synonym(models.Model):
    synonym = models.CharField(max_length=100)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    def __str__(self):
        return self.synonym



    
    