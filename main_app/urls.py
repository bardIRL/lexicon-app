from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('words/', views.words_index, name='index'),
    path('words/<int:word_id>/', views.words_detail, name='detail'),
    path('words/create/', views.WordCreate.as_view(), name='words_create'),
    path('words/<int:pk>/update/', views.WordUpdate.as_view(), name='words_update'),
]