from django.contrib import admin
from .models import Word, NearbyWord

# Register your models here.
admin.site.register(Word)
admin.site.register(NearbyWord)