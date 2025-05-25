from django.contrib import admin
from .models import BusinessProfile, Location, Event

@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_name', 'email', 'is_partner')
    list_filter = ('is_partner',)
    search_fields = ('name', 'contact_name', 'email')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'dock_access', 'courtesy_dock', 'featured')
    list_filter = ('type', 'dock_access', 'courtesy_dock', 'featured')
    search_fields = ('name', 'address')
    raw_id_fields = ('business',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'is_public')
    list_filter = ('is_public', 'date')
    search_fields = ('title',)
