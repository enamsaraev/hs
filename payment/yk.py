import json
import time
import uuid

from yookassa import Configuration, Payment

from payment import config


# Configuration.configure_auth_token('token-XXXXXXXX')
#{"price": "4567.09", "description": "text"}
#test_wE6Q6Zb5FGPWrfJRlg1ynZaj66RKdeYf52CyOzyJ_KE
#967176


#{"price": "123.45", "description": "text"}


Configuration.account_id = 967176
Configuration.secret_key = 'test_wE6Q6Zb5FGPWrfJRlg1ynZaj66RKdeYf52CyOzyJ_KE'


def create_payment(price, description) -> dict:
    """Create a payment"""

    payment = Payment.create({
        "amount": {
            "value": price,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://www.example.com/return_url"
        },
        "capture": True,
        "description": description
    }, uuid.uuid4())

    return json.loads(payment.json())


def check_payment(payment_id) -> bool:
    """Check if payment status is success"""

    payment = json.loads((Payment.find_one(payment_id)).json())

    while payment['status'] == 'pending':
        payment = json.loads((Payment.find_one(payment_id)).json())
        time.sleep(3)

    if payment['status']=='succeeded':
        return True

    elif payment['status'] == 'canceled':
        return False

    return False


