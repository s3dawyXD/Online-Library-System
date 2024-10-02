import django_filters
from .models import Book, Author, Category


class BookFilter(django_filters.FilterSet):
    category_id = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    author_id = django_filters.ModelChoiceFilter(queryset=Author.objects.all())
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Book
        fields = [
            "category_id",
            "author_id",
            "price",
            "year",
            "price_min",
            "price_max",
        ]
