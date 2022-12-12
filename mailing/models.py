from django.db import models

from orders.models import Order

class EmailEntry(models.Model):
    """Email logging"""

    email = models.CharField(max_length=255, null=False)
    message = models.TextField()
    order = models.ForeignKey(
        Order,
        related_name='emails',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.email
