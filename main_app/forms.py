from django.forms import ModelForm
from .models import NearbyWord

class NearbyWordForm(ModelForm):
  class Meta:
    model = NearbyWord
    fields = ['nearby_word']

