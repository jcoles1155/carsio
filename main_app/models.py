from django.db import models
from django.urls import reverse

# Create your models here.
class CarPost(models.Model):
    title = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    carModel = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    year = models.IntegerField()
    body = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

