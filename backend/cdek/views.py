from rest_framework.decorators import api_view
from rest_framework.response import Response

from cdek.helpers import CDEKHelper


@api_view(['POST'])
def get_offices_list(request, *args, **kwargs):
    """Retrieving a list offices in city"""

    ch = CDEKHelper()
    res = ch.get_offices(city=request.data['to_location'])

    if res:
        return Response({'result': res})
    
    return Response({'result': 'Такого города нет'})
