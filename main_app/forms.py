from django.forms import ModelForm
from .models import NearbyWord, Synonym

class NearbyWordForm(ModelForm):
  class Meta:
    model = NearbyWord
    fields = ['nearby_word']

class SynonymForm(ModelForm):
  class Meta:
    model = Synonym
    fields = ['synonym']

