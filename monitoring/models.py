from django.conf import settings
from django.db import models
from django.utils import timezone


class Vulnerability(models.Model):
    name = models.CharField(unique=True, max_length=200, default="")
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    relevance = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'уязвимость'
        verbose_name_plural = 'уязвимости'
        ordering = ['-id']

    def __str__(self):
        return self.title
