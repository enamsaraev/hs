from dataclasses import dataclass

from core.models import ProductInventory


@dataclass
class MsgHelper:
    cart: dict

    def __call__(self):
        """Generate a msg"""

        lst = []

        for item in self.cart['items'].keys():
            product = ProductInventory.objects.get(slug=item)
            size = self.cart['items'][item]['size']
            color = self.cart['items'][item]['color']

            variatiion_info = f'{product.name}: размер {size}, цвет {color}'  
            lst.append(variatiion_info)
        
        return ' '.join(lst)