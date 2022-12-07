import json
import time

from yookassa import Configuration,Payment


# Configuration.account_id = config.SHOP_ID
# Configuration.secret_key = config.SHOP_API_TOKEN


def create_payment(price, description):
    """Create a payment"""

    payment = Payment.create({
    "amount": {
        "value": str(price),
        "currency": "RUB"
    },
    "payment_method_data": {
        "type": "bank_card"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": "урл редиректа"
    },
    "capture": True,
    "description": description
    })

    return json.loads(payment.json())


def check_payment(payment_id):
    """Check if payment status is success"""

    payment = json.loads((Payment.find_one(payment_id)).json())

    while payment['status'] == 'pending':
        payment = json.loads((Payment.find_one(payment_id)).json())
        time.sleep(3)
        
    if payment['status']=='succeeded':
        return True

    else:
        return False


