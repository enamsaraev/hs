from orders.models import Order, OrderItems
from core.models import Variation
from coupon_api.models import Coupon


class OrderComponent:    
    def __init__(self, cart):

        self.cart = cart

    def processing_order(self, data):
        """Main function in creating order"""

        coupon = None

        if 'code' in data:
            coupon=Coupon.objects.get(code=data['code'])
            
        res, order = self.set_order(data, coupon)

        if res:
            self.set_order_data(order)

            return True, order

    def set_order(self, data, coupon):
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

    def set_order_data(self, order):
        """Creates all order items from the cart session""" 

        for item in self.cart:
            var = Variation.objects.get_variation(
                product_slug=item,
                size=self.cart[item]['size'],
                color=self.cart[item]['color']
            )

            var.set_minus_count(self.cart[item]['quantity'])

            OrderItems.objects.create(
                order=order,
                product_variation=var,
                price=var.product.retail_price,
                qunatity=int(self.cart[item]['quantity'])
            )
