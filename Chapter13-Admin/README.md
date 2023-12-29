## Django Admin

Django admin is a built-in application that allows us to manage the Django project. We can CRUD (create, read, update, and delete) the data in the database using the Django admin.

### How to register the model to Django admin

app/admin.py

```python
from django.contrib import admin
from .models import Post


admin.site.register(Post)
```

### How to customize the model in Django admin

app/admin.py

```python
from django.contrib import admin
from .models import Publisher, Author, Book

class BookModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'price', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title', 'authors', 'publisher', 'publication_date')
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book, BookModelAdmin)
```
