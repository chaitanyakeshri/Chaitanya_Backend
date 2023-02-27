from rest_framework import serializers
from home.models import Event


class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
