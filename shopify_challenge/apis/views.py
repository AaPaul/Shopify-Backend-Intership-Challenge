import imp
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getItems(request):
    person = {
        'name': 'Ao',
        'ID': 111
    }
    return Response(person)
    