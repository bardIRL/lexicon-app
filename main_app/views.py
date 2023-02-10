from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Word, NearbyWord
from .forms import NearbyWordForm

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
    nearby_word_form = NearbyWordForm()
    return render(request, 'words/detail.html', {
        'word': word,
        'title': word.word,
        'nearby_word_form': nearby_word_form,
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

def add_nearby_word(request, word_id):
  form = NearbyWordForm(request.POST)
  if form.is_valid():
    new_nearby_word = form.save(commit=False)
    new_nearby_word.word_id = word_id
    new_nearby_word.save()
  return redirect('detail', word_id=word_id)