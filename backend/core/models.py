from django.db import models

class BusinessProfile(models.Model):
    name = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_partner = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    LOCATION_TYPES = [
        ('restaurant', 'Restaurant'),
        ('boat_ramp', 'Boat Ramp'),
        ('marina', 'Marina'),
        ('fuel', 'Fuel Dock'),
        ('event_venue', 'Event Venue'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=LOCATION_TYPES)
    address = models.CharField(max_length=300, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    dock_access = models.BooleanField(default=False)
    courtesy_dock = models.BooleanField(default=False)
    lanes = models.PositiveIntegerField(blank=True, null=True, help_text="For ramps only")
    description = models.TextField(blank=True, null=True)
    business = models.ForeignKey(BusinessProfile, blank=True, null=True, on_delete=models.SET_NULL)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
