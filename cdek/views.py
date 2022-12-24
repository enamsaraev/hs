from rest_framework.decorators import api_view
from rest_framework.response import Response

from cdek.helpers import auth_cdek_and_get_amount


@api_view(['POST'])
def get_offices_list(request, *args, **kwargs):
    """Retrieving a list oif city offices"""

    res = auth_cdek_and_get_amount(to_location=request.data['to_location'])

    return Response({'result': res})


# {"to_location": "44"}