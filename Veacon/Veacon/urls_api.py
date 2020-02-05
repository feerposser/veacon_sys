from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from beacon.api.viewsets import BeaconViewSet
from watchpost.api.viewsets import WatchpostViewSet
from gateway_beacon.api.viewsets import GatewayBeaconViewSet
from alert.api.viewsets import AlertViewSet

router = routers.DefaultRouter()
router.register(r'beacon', BeaconViewSet, base_name='BaconModel')
router.register(r'watchpost', WatchpostViewSet, base_name='WatchpostModel')
router.register(r'alert', AlertViewSet, base_name='AlertModel')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('gateway_beacon/', GatewayBeaconViewSet.as_view()),
]
