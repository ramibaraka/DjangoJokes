from rest_framework import serializers
from api.models import Joke

class JokeSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Joke
        fields = [
            'content',
            'created_on',
            'pk',
        ]