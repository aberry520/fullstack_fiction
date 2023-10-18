from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name