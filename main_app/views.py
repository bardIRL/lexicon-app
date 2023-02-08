from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Word

# Create your views here.

def home(request):
    title = 'Lexicon'
    return render(request, 'home.html', {
        'title': title
    })

def about(request):
    return render(request, 'about.html')

def words_index(request):
    title = 'All Words'
    words = Word.objects.all()
    return render(request, 'words/index.html', {
        'words': words,
        'title': title
    })

def words_detail(request, word_id):
    word = Word.objects.get(id=word_id)
    return render (request, 'words/detail.html', {
        'word': word,
        'title': word.word
    })

class WordCreate(CreateView):
    model = Word
    fields = '__all__'
    success_url = '/words'

class WordUpdate(UpdateView):
    model = Word
    fields = '__all__'
    success_url = '/words'

class WordDelete(DeleteView):
    model = Word
    success_url = '/words'