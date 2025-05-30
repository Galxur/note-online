from django.shortcuts import render
from django.template.defaultfilters import title
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

# Create your views here.

class NoteView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


# class CreateNote(generics.CreateAPIView):
class ViewById(generics.RetrieveAPIView):
    queryset = Note.objects.all().order_by('-id')
    serializer_class = NoteSerializer

#the ListAPIView or ListCreateAPIView is for only viewing all of them
#for viewing by id I have use RetrieveUpdateDestroyAPIView

class CreateNewNote(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

#It can be use for adding new things

class UpdateDeleteNote(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer