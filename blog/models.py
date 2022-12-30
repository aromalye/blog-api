from django.db import models
from accounts.models import Account
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title