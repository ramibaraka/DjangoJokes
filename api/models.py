from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Joke(models.Model):
    content = models.TextField(max_length=240, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
