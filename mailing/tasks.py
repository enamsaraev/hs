from __future__ import absolute_import, unicode_literals

from celery import shared_task
from mailing.pigeon import Pigeon


@shared_task
def send_mail(to: str, message: str, subject: str):
    """Async email sending"""

    Pigeon(
        to=to,
        message=message,
        subject=subject,
    )()
