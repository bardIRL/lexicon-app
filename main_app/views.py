from django.shortcuts import render

words = [
    {
        'word':'uncouth',
        'part_of_speech': 'adjective',
        'definition':'lacking good manners, refinement, or grace, typically in a rude and unpleasant manner',
        'synonyms': 'uncivilized, uncultured, plebeian, rough, unsophisticated',
        'sentence':'She may embarrass you at the dinner party with her typical, uncouth behavior.',
    },
    {
        'word':'peregrinate',
        'part_of_speech': 'verb',
        'definition':'to travel or wander around from place to place, especially on foot',
        'synonyms': 'hike, journey, travel, walk, rove,perambulate',
        'sentence':'We peregrinated over Stanmore, and visited the Castles of Bowes and Brougham.',
    },
    {
        'word':'sanctimonious',
        'part_of_speech': 'adjective',
        'definition':'making a show of being morally superior to other people',
        'synonyms': 'self-righteous, holier-than-thou, churchy, pious, hypocritical, unctuous',
        'sentence':'I could not stand his sanctimonious speech about the importance of sobriety when he gets plastered every other weekend.',
    },
     {
        'word':'obsequious',
        'part_of_speech': 'adjective',
        'definition':'obedient or attentive to an excessive or servile degree',
        'synonyms': 'unctuous, fawning, servile, submissive',
        'sentence':'Barrow was positively obsequious to me until he learned that I too was the son of a laboring man.',
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