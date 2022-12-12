from decimal import Decimal

from rest_framework.exceptions import ParseError


class Cart:
    def __init__(self, request):

        if 'HTTP_TOKEN' not in request.META:
            raise ParseError()

        self._token = request.META.get('HTTP_TOKEN')
        self._session = request.session

        cart = self._session.get(self._token)

        if not cart:
            cart = self._session[self._token] = {
                'items': {},
                'total': 0,
                'discount': 0
            }

        self.cart = cart

    def add_or_update(self, product, quantity, size, color, update) -> None:
        """Add or update a product in the cart"""

        product_slug = product.slug

        if update:
            self.cart['items'][product_slug]['quantity'] = quantity
            self.cart['items'][product_slug]['size'] = size
            self.cart['items'][product_slug]['color'] = color
        else:
            self.cart['items'][product_slug] = {
                'size': size,
                'color': color,
                'quantity': quantity,
                'price': str(product.retail_price),
            }

        self.cart['items'][product_slug]['total_item_price'] = str(Decimal(product.retail_price) * quantity)

        self.get_total_price()

        self.__save()

    def delete(self, product) -> None:
        """Removing a single product from the cart"""

        product_slug = product.slug

        if product_slug in self.cart['items']:
            del self.cart['items'][product_slug]

        self.__save()

    def set_discount(self, discount) -> None:
        """Rewrite total price by a discount"""

        self.cart['discount'] = str(discount)

        self.__save()

    def get_total_price(self) -> None:
        """Retrieving a total cart price"""
        
        if self.cart['discount'] != 0:
            total_sum_without_duscount = sum(
                Decimal(self.cart['items'][item]['total_item_price']) for item in self.cart['items'].keys()
            )
            self.cart['total'] = str(total_sum_without_duscount * int(self.cart['discount']) / 100)
        
        else:
            self.cart['total'] = str(sum(
                    Decimal(self.cart['items'][item]['total_item_price']) for item in self.cart['items'].keys()
                ))

    def get_cart(self) -> dict:
        """Retrieving a full product cart"""
        
        self.get_total_price()
        return self.cart

    def clear_all_cart(self) -> None:
        """Clearing all cart session data"""

        del self._session[self._token] 
        self._session.modified = True

    def __save(self) -> None:
        """Saving current cart session"""

        self._session[self._token] = self.cart
        self._session.modified = True

    def __iter__(self):
        """Iter cart object"""

        for item in self.cart['items']:
            yield item

# {"product_slug": "hoodie-black", "quantity": "2", "update": "True"}