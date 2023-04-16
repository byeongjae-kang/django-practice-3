from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.name} - {self.address}"


class Meetup(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to="images")
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.title} - {self.location}"
