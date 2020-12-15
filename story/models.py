import uuid

from django.db import models
from django.utils import timezone\



class Publisher(models.Model):

    class Meta:
        db_table = 'publisher'
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Book(models.Model):

    class Meta:
        db_table = 'stories'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    story = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
