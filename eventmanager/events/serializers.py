from events.models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'organizer']