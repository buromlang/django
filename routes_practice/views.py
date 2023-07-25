from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from rest_framework.views import APIView


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


class BookView(APIView):
    @method_decorator(cache_page(60*60*3))
    @method_decorator(vary_on_cookie)
    @method_decorator(vary_on_headers("Authorization", 'Host', ))
    def get(self, request, format=None):
        return Response("tested cache")


