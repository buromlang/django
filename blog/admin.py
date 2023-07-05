from django.contrib import admin

# Register your models here.
from .models import Blog, Entry, Author, Student


class EntryAdmin(admin.StackedInline):
    model = Entry
    extra = 1


class BlogAdmin(admin.ModelAdmin):
    inlines = [EntryAdmin]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Author)
admin.site.register(Student)
# admin.site.register(MoonLandings)
