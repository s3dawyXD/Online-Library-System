from django.urls import path

from .views import BookCreate, BookUpdate, BookDetail, BooksList


urlpatterns = [
    path("books/list", BooksList.as_view(), name="books"),
    path("books/<int:pk>/get", BookDetail.as_view(), name="book-detail"),
    path("books/new/", BookCreate.as_view(), name="book-create"),
    path("books/<int:pk>/edit/", BookUpdate.as_view(), name="book-update"),
]
