from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response

from story.models import Book
from apiv1.selializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookListCreateAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        book_list = Book.objects.all()
        serializer = BookSerializer(instance=book_list, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        serializer .is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class BookRetrieveUpdateDestroyAPIView(views.APIView):

    def get(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(instance=book)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, requst, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(instance=book, data=requst.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


