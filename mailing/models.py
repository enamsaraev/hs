from django.db import models


class EmailEntry(models.Model):
    """Email logging"""

    email = models.CharField(max_length=255, null=False)
    message = models.TextField()
