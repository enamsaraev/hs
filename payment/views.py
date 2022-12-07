from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from payment.serializers import PaymentDataSerializer, PaymentIdSerializer
from payment.yk import create_payment, check_payment

from orders.models import Order

@api_view(['GET'])
def get_create_payment(reqeust, *args, **kwargs):
    """Get a redirect url"""

    serializer = PaymentDataSerializer(data=reqeust.data)

    if serializer.is_valid():
        """Create payment"""

        payment_data = create_payment(
            price=serializer.data['price'],
            description=serializer.data['description']
        )

        return Response(
            {
                'url': payment_data['confirmation']['confirmation_url'],
                'id': payment_data['id']
            },
            status==status.HTTP_200_OK
        )

    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_success_payment(request, *args, **kwargs):
    """Retrun payment success info"""

    serializer = PaymentIdSerializer(data=request.data)

    if serializer.is_valid():
        """Check if payment is successful"""

        success = check_payment(id=serializer.data['id'])

        if success:
            order = Order.objects.get() ## узнать как тянуть
            order.set_updates(serializer.data['id'])

            return Response(status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

