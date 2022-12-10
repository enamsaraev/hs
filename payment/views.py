from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from orders.models import Order

from payment.models import PaymentData
from payment.serializers import PaymentIdSerializer
from payment.yk import create_payment, check_payment


@api_view(['POST'])
def get_create_payment(request, *args, **kwargs):
    """Get a redirect url"""

    payment_data = create_payment(
        price=request.data['price'],
        description=request.data['description'],
    )

    order = Order.objects.get(id=request.data['id'])
    order.set_payment_id(payment_data['id'])

    return Response(
        {
            'url': payment_data['confirmation']['confirmation_url'],
            'id': payment_data['id']
        },
        status==status.HTTP_200_OK
    )


@api_view(['POST'])
def get_success_payment(request, *args, **kwargs):
    """Retrun payment success info"""
    """Check if payment is successful"""

    success = check_payment(id=request.data['payment_id'])

    if success:
        order = Order.objects.get(id=request.data['order_id'])
        PaymentData.objects.create(
            payment_id=request.data['payment_id'],
            order=order
        )
        # celery deley
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

