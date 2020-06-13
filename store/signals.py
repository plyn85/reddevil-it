from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import OrderItem


@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on orderitem """

    instance.order.get_cart_total()
