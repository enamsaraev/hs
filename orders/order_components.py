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
            
        order = self.set_order(data, coupon)

        if order:
            self.set_order_data(order)

            return order

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
        
        cart = self.cart.get_cart()
        
        for item in cart['items']:
            var = Variation.objects.get_variation(
                product_slug=item,
                size=cart['items'][item]['size'],
                color=cart['items'][item]['color'],
            )

            var.set_minus_count(cart['items'][item]['quantity'])

            OrderItems.objects.create(
                order=order,
                product_variation=var,
                price=var.product.retail_price,
                qunatity=int(cart['items'][item]['quantity'])
            )


#{"name": "name", "email": "mail@mail.com", "phone": "89001009988", "coupon_discount": "0", "total_price": "194.00"}