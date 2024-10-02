from django.test import TestCase
from .models import Book, Author, Category


class TestBooks(TestCase):
    def setUp(self) -> None:
        self.author = Author.objects.create(name="Test Author3")
        self.category = Category.objects.create(name="Test Category3")
        self.book = Book.objects.create(
            title="Test Book",
            author=Author.objects.create(name="Test Author"),
            category=Category.objects.create(name="Test Category"),
        )

        self.book_2 = Book.objects.create(
            title="Test Book 2",
            author=Author.objects.create(name="Test Author 2"),
            category=Category.objects.create(name="Test Category 2"),
        )

    def test_books_list(self):
        book_count = Book.objects.count()
        response = self.client.get("/books/list")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data.get("results")), book_count)

    def test_book_detail(self):
        response = self.client.get(f"/books/{self.book.id}/get")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Test Book")

    def test_book_create(self):
        old_count = Book.objects.count()
        response = self.client.post(
            "/books/new/",
            {
                "title": "Test Book 3",
                "author": self.author.id,
                "category": self.category.id,
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), old_count + 1)

    def test_book_update(self):
        response = self.client.patch(
            "/books/1/edit/", {"title": "Test Book 3"}, content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Book.objects.get(id=self.book.id).title, "Test Book 3")
