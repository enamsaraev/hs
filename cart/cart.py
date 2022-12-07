import json

from decimal import Decimal


class Cart:
    def __init__(self, session, token):
        self._token = token
        self._session = session

        cart = self._session.get(self._token)

        if not cart:
            cart = self._session[self._token] = {}

        self.cart = cart

    def add_or_update(self, product, quantity, size, color, update):
        """Add or update a product in the cart"""
        
        product_slug = product.slug

        if product_slug not in self.cart:
            self.cart[product_slug] = {
                'quantity': 0,
                'size': '',
                'color': '',
                'price': str(product.retail_price)
            }

        if update:
            self.cart[product_slug]['quantity'] = quantity
            self.cart[product_slug]['size'] = size
            self.cart[product_slug]['color'] = color

        else:
            self.cart[product_slug]['quantity'] += quantity
            self.cart[product_slug]['size'] = size
            self.cart[product_slug]['color'] = color

        self.__save()

    def delete(self, product):
        """Removing a single product from the cart"""

        product_slug = product.slug

        if product_slug in self.cart:
            del self.cart[product_slug]

        self.__save()

    def clear_all_cart(self):
        """Clearing all cart session data"""

        del self._session[self._token] 
        self._session.modified = True

    def __save(self):
        """Saving current cart session"""

        self._session[self._token] = self.cart
        self._session.modified = True

    def get_cart(self):
        """Retrieving a full product cart"""

        cart = self.cart

        return cart

    def get_total_price(self):
        """Retrieving a total cart price"""
        
        return str(sum(Decimal(self.cart[item]['price']) * self.cart[item]['quantity'] for item in self.cart.keys()))


    def __iter__(self):
        """Iter cart object"""

        for item in self.cart:
            yield item

# {"product_slug": "hoodie-black", "quantity": "2", "update": "True"}