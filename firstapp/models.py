from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    subject = models.CharField(max_length=50, blank=True)
    article = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.subject
