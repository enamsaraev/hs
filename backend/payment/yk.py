import json
import uuid

from yookassa import Configuration, Payment

Configuration.account_id = 967176
Configuration.secret_key = 'test_wE6Q6Zb5FGPWrfJRlg1ynZaj66RKdeYf52CyOzyJ_KE'


def create_payment(price: str, description: str) -> dict:
    """Create a payment"""

    payment = Payment.create({
        "amount": {
            "value": price,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://eveclothes.ru"
        },
        "capture": True,
        "description": description
    }, uuid.uuid4())

    return json.loads(payment.json())




