from django.db import models
from django.contrib.auth.models import User


class Text(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Comment(models.Model):
    texts = models.ForeignKey(Text, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()