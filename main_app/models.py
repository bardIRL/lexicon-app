from django.db import models
from django.urls import reverse

PARTS_OF_SPEECH = (
    ('noun','noun'),
    ('verb','verb'),
    ('adjective','adjective'),
    ('adverb','adverb')
)

CONNOTATIONS = (
    ('positive', 'Positive'),
    ('negative', 'Negative'),
    ('neutral', 'Neutral')
)

COLORS = (
    ('red', 'Red'),
    ('orange', 'Orange'),
    ('green','Green'),
    ('blue', 'Blue'),
    ('purple', 'Purple'),
    ('pink', 'Pink')
)


# Create your models here.
class Label(models.Model):
    name = models.CharField(max_length=100)
    memo = models.TextField(max_length=250)
    color = models.CharField(
        max_length=100,
        choices=COLORS
    )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('labels_detail', kwargs={'pk': self.id})

class Word(models.Model):
    word = models.CharField(max_length=100)
    part_of_speech = models.CharField(
        max_length=100,
        choices=PARTS_OF_SPEECH,
    )
    definition = models.TextField(max_length=300)
    etymology = models.CharField(max_length=250)
    connotation = models.CharField(
        max_length=100,
        choices=CONNOTATIONS,
        )
    sentence = models.TextField(max_length=300)
    labels = models.ManyToManyField(Label)

    def __str__(self):
        return self.word

    def get_absolute_url(self):
        return reverse('detail', kwargs={'word_id': self.id})

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



    
    