from rest_framework import viewsets, filters
from .models import BusinessProfile, Location, Event
from .serializers import BusinessProfileSerializer, LocationSerializer, EventSerializer

class BusinessProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to list or retrieve business profiles.
    """
    queryset = BusinessProfile.objects.all()
    serializer_class = BusinessProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'contact_name', 'email']

class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to list or retrieve locations (restaurants, ramps, marinas).
    """
    queryset = Location.objects.select_related('business').all()
    serializer_class = LocationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'address']
    ordering_fields = ['type', 'featured', 'name']

class EventViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to list or retrieve upcoming events.
    """
    queryset = Event.objects.select_related('location').all()
    serializer_class = EventSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date', 'title']
