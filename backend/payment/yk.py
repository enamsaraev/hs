import os
import json
import uuid

from dotenv import load_dotenv
from yookassa import Configuration, Payment

load_dotenv()


Configuration.account_id = os.environ.get("Y_ID")
Configuration.secret_key = os.environ.get("Y_KEY")

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




