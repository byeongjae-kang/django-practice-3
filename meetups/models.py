from django.db import models

# Create your models here.


class Meetup(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.title} - {self.location}"
