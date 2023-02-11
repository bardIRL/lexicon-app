from django.contrib import admin
from .models import Word, NearbyWord, Synonym, Label

# Register your models here.
admin.site.register(Word)
admin.site.register(NearbyWord)
admin.site.register(Synonym)
admin.site.register(Label)