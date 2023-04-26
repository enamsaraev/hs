from __future__ import absolute_import, unicode_literals

import json, time
from typing import List

from yookassa import Payment
from celery import shared_task

from ecommerce_celery.celery import app

from mailing.pigeon import Pigeon, PigeonAutomaticly
from mailing.models import EmailSendAutomaticly, EmailSendTemplate


def check_succed_payment_retr(payment_id: str):
    """Checking if order is paid"""

    payment = Payment.find_one(payment_id)

    while payment['status'] == 'pending' and payment['status'] != 'canceled':
        payment = Payment.find_one(payment_id)
        time.sleep(3)

    if payment['status']=='succeeded':
        return True

    return False


@shared_task
def send_mail(payment_id: str, to: List[str], message: str, subject: str, order_id: int):
    """Async email sending"""
    
    if check_succed_payment_retr(payment_id):
        
        Pigeon(
            to=to,
            text=message,
            subject=subject,
            order_id=order_id,
        ).call_pigeon()

    else:
        print('Mail fucked')


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
