from django.shortcuts import render

from .models import Word

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def words_index(request):
    words = Word.objects.all()
    return render(request, 'words/index.html', {
        'words': words
    })

def words_detail(request, word_id):
    word = Word.objects.get(id=word_id)
    return render (request, 'words/detail.html', {
        'word': word
    })
    