# Generated by Django 5.1.1 on 2024-10-02 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_price_book_release_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='release_date',
        ),
    ]
