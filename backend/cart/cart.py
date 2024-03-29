from decimal import Decimal
from rest_framework.exceptions import ParseError

from core.models import Media

# {"product_slug": "hyi", "quantity": "1", "size": "S", "color": "Black", "update": "False"}
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
                'total': '',
                'discount': {}
            }

        self.cart = cart

    def add_or_update(self, product: object, quantity: int, size: str, color: str, update: bool) -> None:
        """Add or update a product in the cart"""

        product_slug = f'{product.slug}/{size}/{color}'
        slug = product.slug
        product_name = product.name
        product_price = product.retail_price
        product_img = Media.objects.filter(product__slug=slug).first()

        if update and product_slug in self.cart:
            
            self.cart['items'][product_slug]['name'] = product_name
            self.cart['items'][product_slug]['slug'] = slug
            self.cart['items'][product_slug]['img'] = product_img.img.url
            self.cart['items'][product_slug]['quantity'] = quantity
            self.cart['items'][product_slug]['size'] = size
            self.cart['items'][product_slug]['color'] = color

        if product_slug not in self.cart:
            self.cart['items'][product_slug] = {
                'name': product_name,
                'slug': slug,
                'img': product_img.img.url,
                'size': size,
                'color': color,
                'quantity': quantity,
                'price': str(product_price),
            }

        self.__item_price_set(product_slug, product_price, quantity)
        self.__save()

    def delete(self, product_slug: str) -> None:
        """Removing a single product from the cart"""

        if product_slug in self.cart['items']:
            del self.cart['items'][product_slug]

            self.__save()

    def set_discount(self, code: str, discount: int) -> None:
        """Rewrite total price by a discount"""

        if not self.cart['discount']:
            self.cart['discount']['code'] = code
            self.cart['discount']['percent'] = discount
            self.cart['discount']['purchased'] = True

            self.__save()

    def __check_coupon(self) -> None:
        """Check if coupon is purchased"""
        
        if self.cart['discount']:
            self.__item_price_set_with_discount()

    def __item_price_set(self, product_slug: str, product_price: Decimal, quantity: int):
        """Set item price"""
        
        self.cart['items'][product_slug]['total_item_price'] = str(Decimal(product_price) * quantity)

    def __item_price_set_with_discount(self):
        """Set item price with discount"""

        for item in self.cart['items'].keys():
            item_price = Decimal(self.cart['items'][item]['total_item_price'])
            self.cart['items'][item]['total_item_price_with_dsc'] = str(item_price * (100-self.cart['discount']['percent']) / 100)

    def __get_total_price(self) -> None:
        """Retrieving a total cart price"""

        if self.cart['discount']:
            self.cart['total'] = str(sum(
                Decimal(self.cart['items'][item]['total_item_price_with_dsc']) for item in self.cart['items'].keys()
            ))
        else:
            self.cart['total'] = str(sum(
                Decimal(self.cart['items'][item]['total_item_price']) for item in self.cart['items'].keys()
            ))

    def get_cart(self) -> dict:
        """Retrieving a full product cart"""
        
        self.__check_coupon()
        self.__get_total_price()

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


{"product_slug": "h", "quantity": "2", "size": "S", "color": "Black", "update": "False"}
{"name": "aa", "email": "enamsaraev@bk.ru", "phone": "111", "total_price": "888", "address": "azaza", "delivery_price": "111"} 