from rest_framework.response import Response
from rest_framework.decorators import api_view
from home.models import Event
from .serializers import EventSerializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


@api_view(['GET'])
def getEvent(request):
    # person = {'name': 'Dennis', 'age': 28}
    items = Event.objects.all()
    serializer = EventSerializers(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addEvent(request):
    serializer = EventSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
def updateEvent(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializers(instance=event, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['DELETE', 'GET'])
def deleteEvent(request, pk):
    item = get_object_or_404(Event, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
