from __future__ import unicode_literals

from django.db import models

class Joke(models.Model):
    content = models.TextField(max_length=240, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
