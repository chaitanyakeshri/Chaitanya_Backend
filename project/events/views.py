from django.http import JsonResponse
from .models import Event
from .serializers import EventSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def event_list(request, format=None):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['PUT'])
def add_item(request, id, format=None):
    event = Event.objects.get(pk=id)
    serializer = EventSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_item(request, id, format=None):
    event = Event.objects.get(pk=id)
    event.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
