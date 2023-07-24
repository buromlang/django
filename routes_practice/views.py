from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['get', 'post'])
    def mark_as_read(self, request, pk=None):
        book = self.get_object()
        book.is_read = True
        book.save()
        return Response({'status': 'success', 'message': 'Book marked as read'})

    def partial_update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = BookSerializer(obj, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def authors(self, request, pk=None):
        return Response({'list': ['burom', 'burom1']})




