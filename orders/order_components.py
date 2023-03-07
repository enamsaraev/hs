from dataclasses import dataclass

from orders.models import Order, OrderItems
from core.models import Variation
from coupon_api.models import Coupon


class OrderComponent:    
    def __init__(self, cart):

        self.cart = cart

    def processing_order(self, data: dict):
        """Main function in creating order"""

        coupon = None

        if 'code' in data:
            coupon=Coupon.objects.get(code=data['code'])
            
        order = self.set_order(data, coupon)

        return order

    def set_order(self, data: dict, coupon: object):
        """Create order"""

        order = Order.objects.create(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            coupon=coupon,
            coupon_discount=data['coupon_discount'],
            total_price=data['total_price']
        )

        if order:
            return order

        else:
            return None
        

@dataclass
class OrderSetCount:
    cart: dict
    order_id: int

    def __call__(self):
        """Creates all order items from the cart session""" 
        order = Order.objects.get(id=self.order_id)
        
        for item in self.cart['items']:
            var = Variation.objects.get_variation(
                product_slug=item.split('/')[0],
                size=self.cart['items'][item]['size'],
                color=self.cart['items'][item]['color'],
            )

            var.set_minus_count(self.cart['items'][item]['quantity'])

            OrderItems.objects.create(
                order=order,
                product_variation=var,
                price=var.product.retail_price,
                qunatity=int(self.cart['items'][item]['quantity'])
            )


#{"name": "name", "email": "mail@mail.com", "phone": "89001009988", "coupon_discount": "0", "total_price": "194.00"}