from django.urls import path
from .views import NoteView , ViewById, CreateNewNote, UpdateDeleteNote

urlpatterns = [
    path('', NoteView.as_view(), name='note-view'),
    path('view/<int:pk>/',ViewById.as_view(), name='view'),
    path('create/', CreateNewNote.as_view(), name='note-create'),
    path('modify/<int:pk>/',UpdateDeleteNote.as_view(), name='note-modify'),
]
