from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


LEXERS = [item for item in get_all_lexers() if item[1]]
# print(LEXERS[1])
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# print(LANGUAGE_CHOICES)
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(blank=True, default='')
    code = models.TextField(default='')
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python')
    style = models.CharField(choices=STYLE_CHOICES, default='friendly')

    owner = models.ForeignKey('auth.user', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        formatter = HtmlFormatter(style=self.style, linenos=linenos)
        self.highlighted = highlight(code=self.code, lexer=lexer, formatter=formatter)
        super().save(*args, **kwargs)


class AppUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    def set_password(self):
        pass
