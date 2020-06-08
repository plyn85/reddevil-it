from django.db import models
from users.models import Profile
from django.contrib.auth.models import User
import uuid


class Product(models.Model):
    name = models.CharField(max_length=254, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Order(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='customer_profile')
    full_name = models.CharField(max_length=254, null=False, default="")
    email = models.EmailField(max_length=254, null=False, default="")
    phone_number = models.CharField(
        max_length=20, null=False, blank=False, default="")
    country = models.CharField(
        max_length=40, null=False, blank=False, default="")
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(
        max_length=40, null=False, blank=False, default="")
    street_address1 = models.CharField(
        max_length=80, null=False, blank=False, default="")
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(
        max_length=32, null=False, editable=False, default="")

    @property
    def get_cart_total(self):
        """Getting all the order items then looping trough them to get the total value  
         _set.all gives the reverse relasionship to all here
        """
        # querying the child order items
        orderitems = self.orderitem_set.all()
        # looping trough orders and getting the totals

        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        """Getting all the order items then looping trough them to get the total quantity """
        # querying the child order items
        orderitems = self.orderitem_set.all()
        # looping trough items and getting the total num

        total = sum([item.quantity for item in orderitems])
        return total

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
        Product, null=False, blank=False, on_delete=models.CASCADE, default="")
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        """ gets the total for each item an multiplys by the the quatity """
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return f'{self.product.name} on order {self.order.transaction_id}'
