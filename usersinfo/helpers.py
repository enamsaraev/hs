from dataclasses import dataclass

from orders.models import Order
from usersinfo.models import CustomerInfo

@dataclass
class CusrtomerInfoSetter:
    name: str
    email: str
    phone: str
    order_id: int

    def __call__(self, *args, **kwds) -> None:
        """Creates an userinfo model"""

        self.order = Order.objects.get(id=self.order_id)

        if not self._check_on_exsisting():
            """Only if False"""
            self._create_new_customer()
        
        else:
            self._add_new_order_to_the_exsisting_customer()

    def _check_on_exsisting(self) -> bool:
        """Check if customer is already exists"""

        return CustomerInfo.objects.get(
            name=self.name,
            email=self.email,
            phone=self.phone,
        ).exsists()
    
    def _add_new_order_to_the_exsisting_customer(self) -> None:
        """New order adding"""
        
        cc = CustomerInfo.objects.get(
                name=self.name,
                email=self.email,
                phone=self.phone,
            )
        cc.order.add(self.order)

    def _create_new_customer(self):
        """New customer creation"""

        nc = CustomerInfo.objects.create(
            name=self.name,
            email=self.email,
            phone=self.phone,
        )
        nc.order.add(self.order)

