from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
