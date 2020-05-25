from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=254, null=True)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=254, null="True")
    email = models.CharField(max_length=254, null="True")

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
#    getting the value of each item or items ordered

    def get_total(self):
        total = self.price * self.quantity
        return total
