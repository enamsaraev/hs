import json
import time

from yookassa import Configuration, Payment

from payment import config


Configuration.configure_auth_token('token-XXXXXXXX')
#{"price": "4567.09", "description": "text"}


def create_payment(price, description) -> dict:
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
        "return_url": "/"
    },
    "capture": True,
    "description": description,
    "receipt": {
            "customer": {
                "full_name": "Ivanov Ivan Ivanovich",
                "email": "email@email.ru",
                "phone": "79211234567",
                "inn": "6321341814"
            },
            "items": [
                {
                    "description": "Переносное зарядное устройство Хувей",
                    "quantity": "1.00",
                    "amount": {
                        "value": 1000,
                        "currency": "RUB"
                    },
                }
            ]
    }
    })

    return json.loads(payment.json())


def check_payment(payment_id) -> bool:
    """Check if payment status is success"""

    payment = json.loads((Payment.find_one(payment_id)).json())

    while payment['status'] == 'pending':
        payment = json.loads((Payment.find_one(payment_id)).json())
        time.sleep(3)

    if payment['status']=='succeeded':
        return True

    else:
        return False


