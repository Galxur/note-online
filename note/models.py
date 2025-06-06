from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=100, unique=False)
    def __str__(self):
        return self.title