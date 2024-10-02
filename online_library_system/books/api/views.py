from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from books.models import Book
from books.api.serializers import BookSerializer


class BookViewSet(viewsets.ViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()

    @action(detail=False, methods=["post"])
    def new(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"], url_path="list")
    def _list(self, request):
        queryset = self.get_queryset()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"], url_path="get")
    def _get(self, request, pk):
        queryset = self.get_queryset()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    @action(detail=True, methods=["patch"])
    def edit(self, request, pk):
        queryset = self.get_queryset()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
