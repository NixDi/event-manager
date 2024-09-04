from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Event
from events.serializers import EventSerializer
from .utils import send_registration_email

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'location']

    @action(detail=True, methods=['post'])
    def register(self, request, pk=None):
        event = self.get_object()
        event.attendees.add(request.user)
        send_registration_email(request.user, event)
        return Response({'status': 'registered'})

    @action(detail=True, methods=['post'])
    def unregister(self, request, pk=None):
        event = self.get_object()
        if request.user in event.attendees.all():
            event.attendees.remove(request.user)
            return Response({'status': 'unregistered'})
        else:
            return Response({'status': 'not registered'}, status=status.HTTP_400_BAD_REQUEST)