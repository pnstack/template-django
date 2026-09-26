from django.urls import path
from rest_framework import routers

from .views import ping

router = routers.DefaultRouter()
urlpatterns = [
    *router.urls,
    path("example/ping", ping, name="ping"),
]
