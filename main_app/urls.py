from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('words/', views.words_index, name='index'),
    path('words/<int:word_id>/', views.words_detail, name='detail'),
    path('words/create/', views.WordCreate.as_view(), name='words_create'),
    path('words/<int:pk>/update/', views.WordUpdate.as_view(), name='words_update'),
    path('words/<int:pk>/delete/', views.WordDelete.as_view(), name='words_delete'),
    path('words/<int:word_id>/add_synonym/', views.add_synonym, name='add_synonym'),
    path('words/<int:word_id>/add_nearby_word/', views.add_nearby_word, name='add_nearby_word'),
    path('words/<int:word_id>/assoc_label/<int:label_id>/', views.assoc_label, name='assoc_label'),
    path('words/<int:word_id>/unassoc_label/<int:label_id>/', views.unassoc_label, name='unassoc_label'),
    path('labels/', views.LabelList.as_view(), name='labels_index'),
    path('labels/<int:pk>/', views.LabelDetail.as_view(), name='labels_detail'),
    path('labels/create/', views.LabelCreate.as_view(), name='labels_create'),
]