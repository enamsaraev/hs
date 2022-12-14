from dataclasses import dataclass

from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from coupon_api.models import Coupon


class CouponHelper:
    def __init__(self):
        self.coupon = None

    def set_coupon(self, code: str):
        """Get coupon from db"""

        time_now = timezone.now()
        try:
            self.coupon = Coupon.objects.get(
                code__iexact=code,
                valid_from__lte=time_now,
                valid_to__gte=time_now,
                is_active=True
            )
            print(self.coupon)

        except ObjectDoesNotExist:
            return 'None'

        return self.__return_discount()

    def __return_discount(self):
        """Return coupon discount"""
        if self.coupon.get_count() == 0:
            return 'Expired'

        self.coupon.set_minus_count()

        return self.coupon.discount

    
