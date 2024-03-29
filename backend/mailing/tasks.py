from __future__ import absolute_import, unicode_literals

import json, time
from typing import List

from yookassa import Payment
from celery import shared_task

from ecommerce_celery.celery import app

from mailing.pigeon import Pigeon, PigeonAutomaticly
from mailing.models import EmailSendAutomaticly, EmailSendTemplate


@shared_task
def send_mail(payment_id: str, to: List[str], message: str, subject: str, order_id: int):
    """Async email sending"""

    payment = json.loads((Payment.find_one(payment_id)).json())
    
    if payment['status'] == 'succeeded':
        Pigeon(
            to=to,
            text=message,
            subject=subject,
            order_id=order_id,
        ).call_pigeon()
    else:
        Pigeon(
            to=to,
            text='None',
            subject=subject,
            order_id=order_id,
        ).call_pigeon()



@shared_task
def send_mail_wia_admin_automaticly(email_id: int, to: List[str], message: str, subject: str, template: str = None):
    """Async email sending wia admin panel"""
       
    PigeonAutomaticly(
        to=to,
        text=message,
        subject=subject,
        template_name=template,
    ).call_pigeon()

    automatic_email = EmailSendAutomaticly.objects.get(id=email_id)
    automatic_email.deliered = True
    automatic_email.save()
