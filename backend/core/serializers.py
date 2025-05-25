from rest_framework import serializers
from .models import BusinessProfile, Location, Event

class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = [
            'id',
            'name',
            'contact_name',
            'email',
            'phone',
            'website',
            'description',
            'is_partner',
            'notes',
        ]

class LocationSerializer(serializers.ModelSerializer):
    business = BusinessProfileSerializer(read_only=True)

    class Meta:
        model = Location
        fields = [
            'id',
            'name',
            'type',
            'address',
            'latitude',
            'longitude',
            'phone',
            'website',
            'dock_access',
            'courtesy_dock',
            'lanes',
            'description',
            'business',
            'featured',
        ]

class EventSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'date',
            'location',
            'is_public',
            'website',
            'created_at',
        ]
