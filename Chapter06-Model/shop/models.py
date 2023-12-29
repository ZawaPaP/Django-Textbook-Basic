from django.db import models


class Publisher(models.Model):

    class Meta:
        db_table = 'publisher'

        name = models.CharField(max_length=255)

        def __str__(self):
            return self.name


class Author(models.Model):

    class Meta:
        db_table = 'author'

        name = models.CharField(max_length=255)

        def __str__(self):
            return self.name


class Book(models.Model):

    class Meta:
        db_table = 'book'

        title = models.CharField(max_length=255, unique=True)
        price = models.IntegerField(null=True, blank=True)
        publisher = models.ForeignKey(
            Publisher,
            on_delete=models.CASCADE,
        )
        authors = models.ManyToManyField(
            Author,
        )
        description = models.TextField(null=True, blank=True)
        publisher_date = models.DateField()

        def __str__(self):
            return self.name


class BookStock(models.Model):

    class Meta:
        db_table = 'book_stock'

        book = models.OneToOneField(
            Book,
            on_delete=models.CASCADE,
        )
        quantity = models.IntegerField(default=0)

        def __str__(self):
            return self.name
