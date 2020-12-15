from rest_framework import serializers

from story.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['author', 'title', 'story', 'publisher']



