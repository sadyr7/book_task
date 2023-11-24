from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['GET'])
    def get_book_by_id(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
            serializer = self.get_serializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({'detail': 'Book not found.'}, status=404)