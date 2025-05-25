from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from core.views import BusinessProfileViewSet, LocationViewSet, EventViewSet

router = routers.DefaultRouter()
router.register(r'businesses', BusinessProfileViewSet, basename='business')
router.register(r'locations',  LocationViewSet,       basename='location')
router.register(r'events',     EventViewSet,          basename='event')

urlpatterns = [
    # Homepage
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
