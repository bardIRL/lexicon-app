from django.shortcuts import render

words = [
    {
        'word':'uncouth',
        'part_of_speech': 'adjective',
        'definition':'lacking good manners, refinement, or grace, typically in a rude and unpleasant manner',
        'sentence':'She may embarrass you at the dinner party with her typical, uncouth behavior.',
    },
    {
        'word':'onomatopoeia',
        'part_of_speech': 'noun',
        'definition':'the formation of a word from a sound associated with what is named',
        'sentence':'The cat breed "Mao" is an obvious example of onomatopoeia, since cats go "Mao".',
    },
    {
        'word':'sanctimonious',
        'part_of_speech': 'adjective',
        'definition':'making a show of being morally superior to other people',
        'sentence':'I could not stand his sanctimonious speech about the importance of sobriety when he gets plastered every other weekend.',
    },

]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def words_index(request):
    return render(request, 'words/index.html', {
        'words': words
    })