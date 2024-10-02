from books.models import Book
from books.api.serializers import BookSerializer
from books.filters import BookFilter
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


class BooksList(generics.ListAPIView):
    model = Book
    serializer_class = BookSerializer
    filterset_class = BookFilter
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["title", "author__name", "category__name"]
    queryset = Book.objects.all()


class BookDetail(generics.RetrieveAPIView):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookUpdate(generics.UpdateAPIView):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = []


class BookCreate(generics.CreateAPIView):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = []
