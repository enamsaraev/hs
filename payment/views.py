from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from orders.models import Order

from payment.serializers import OrderIdSerializer
from payment.yk import create_payment
from payment.tasks import check_payments_status

from mailing.tasks import send_mail


@api_view(['POST'])
def get_create_payment(request, *args, **kwargs) -> Response:
    """Get a redirect url"""

    payment_data = create_payment(
        price=request.data['price'],
        description=request.data['description'],
    )

    check_payments_status.delay(
        payment_id=payment_data['id'],
        order_id=int(request.data['id'])
    )

    return Response(
        {
            'url': payment_data['confirmation']['confirmation_url'],
            'id': payment_data['id']
        },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def send_notification_mail_with_payed_order(request, *args, **kwargs) -> Response:
    """Retrun payment success info"""
    """Check if payment is successful"""

    serializer = OrderIdSerializer(data=request.data)
    
    if serializer.is_valid():
        order = Order.objects.get(id=serializer.data['id'])
        
        send_mail.delay(
            to='test@mail.com',
            message='Спасибо за покупку!',
            subject=f'BABYEVE Заказ №{order.id}',
            order_id=order.id
        )
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)

    

# {"id": "12", "price": "194.00", "description": "text"}