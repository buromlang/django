from django.db import models
from datetime import date
# Create your models here.
from django.urls import reverse


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    time_field = models.TimeField(null=True, auto_now=False, auto_now_add=True)
    time_field_auto_f = models.TimeField(null=True, auto_now=True, auto_now_add=False)
    now = models.DateField(default=date.today())

    def __str__(self):
        return self.question_text


class Article(models.Model):
    headline = models.CharField(max_length=100)
    content = models.TextField()
    reporter = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    today_date = models.DateField(default=date.today())
    slug = models.SlugField(unique=True, null=True, allow_unicode=True)

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={'pk': self.pk})


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.manufacturer_name

    def get_absolute_url(self):
        return reverse("manufacturer-detail", kwargs={'pk': self.pk})
