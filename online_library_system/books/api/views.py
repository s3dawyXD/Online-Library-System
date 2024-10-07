from books.models import Book, Author, Category
from books.api.serializers import BookSerializer, AuthorSerializer, CategorySerializer
from books.filters import BookFilter
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets


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


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = []


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []
