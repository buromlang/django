from django.db import models

# Create your models here.
# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
