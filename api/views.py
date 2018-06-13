from __future__ import unicode_literals

from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from api.models import Joke
from api.serializers import JokeSerializer

def ping(request):
    return HttpResponse('Ping !') 


class JokeListView(generics.ListCreateAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class JokeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JokeSerializer
    queryset = Joke.objects.all()



