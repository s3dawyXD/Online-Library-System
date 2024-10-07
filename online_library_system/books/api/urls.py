from django.urls import path, include
from rest_framework import routers

from .views import (
    BookCreate,
    BookUpdate,
    BookDetail,
    BooksList,
    AuthorViewSet,
    CategoryViewSet,
)


router = routers.DefaultRouter()
router.register(r"authors", AuthorViewSet, basename="authors")
router.register(r"categories", CategoryViewSet, basename="categories")

urlpatterns = [
    path("books/list", BooksList.as_view(), name="books"),
    path("books/<int:pk>/get", BookDetail.as_view(), name="book-detail"),
    path("books/new/", BookCreate.as_view(), name="book-create"),
    path("books/<int:pk>/edit/", BookUpdate.as_view(), name="book-update"),
] + router.urls
