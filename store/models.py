from django.db import models
from users.models import Profile
from django.contrib.auth.models import User
import uuid
from django_countries.fields import CountryField
from django.db.models import Sum


class Product(models.Model):
    name = models.CharField(max_length=254, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                                null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, default="")
    phone_number = models.CharField(
        max_length=20, null=False, blank=False, default="")
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(
        max_length=40, null=False, blank=False, default="")
    street_address1 = models.CharField(
        max_length=80, null=False, blank=False, default="")
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(
        max_length=32, null=False, editable=False)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def get_cart_total(self):
        """Update total each time a item Is added
        """
        self.total = self.orderitems.aggregate(Sum('orderitem_total'))[
            'orderitem_total__sum']or 0
        self.total
        self.save()

    def _generate_transaction_id(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.transaction_id:
            self.transaction_id = self._generate_transaction_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.transaction_id


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE,  default="")
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, related_name="orderitems",)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    orderitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False, default=0)

    def save(self, *args, **kwargs):
        """ gets the total for each item an multiplys by the the quatity """
        self.orderitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} on order {self.order.transaction_id}'
