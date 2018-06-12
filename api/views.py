from __future__ import unicode_literals

from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from models import Joke
from serializers import JokeSerializer

def ping(request):
    return HttpResponse('Ping !') 

class JokeGenericView():
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class JokeListView(JokeGenericView, generics.ListCreateAPIView):
    pass

class JokeDetailView(JokeGenericView, generics.RetrieveUpdateDestroyAPIView):
    pass



