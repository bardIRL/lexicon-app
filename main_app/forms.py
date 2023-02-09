from django.forms import ModelForm
from .models import Synonym

class SynonymForm(ModelForm):
  class Meta:
    model = Synonym
    fields = ['synonym']

