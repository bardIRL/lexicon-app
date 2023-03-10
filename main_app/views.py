from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Word, Label
from .forms import NearbyWordForm, SynonymForm

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
    id_list = word.labels.all().values_list('id')
    unassociated_labels = Label.objects.exclude(id__in=id_list)
    nearby_word_form = NearbyWordForm()
    synonym_form = SynonymForm()
    print(unassociated_labels)
    return render(request, 'words/detail.html', {
        'word': word,
        'title': word.word,
        'nearby_word_form': nearby_word_form,
        'synonym_form': synonym_form,
        'labels': unassociated_labels
    })

class WordCreate(CreateView):
    model = Word
    fields = ['part_of_speech','definition','word','etymology','connotation','sentence']
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

def add_synonym(request, word_id):
    form = SynonymForm(request.POST)
    if form.is_valid():
        new_synonym = form.save(commit=False)
        new_synonym.word_id = word_id
        new_synonym.save()
    return redirect('detail', word_id=word_id)

class LabelList(ListView):
    model = Label

class LabelDetail(DetailView):
    model = Label
    
class LabelCreate(CreateView):
    model = Label
    fields = '__all__'

def assoc_label(request, word_id, label_id):
    Word.objects.get(id=word_id).labels.add(label_id)
    return redirect('detail', word_id=word_id)

def unassoc_label(request, word_id, label_id):
    Word.objects.get(id=word_id).labels.remove(label_id)
    return redirect('detail', word_id=word_id)