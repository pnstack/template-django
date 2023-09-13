from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework_nested import routers
from django.urls import path
from rest_framework.response import Response
from .views import ping
router = routers.DefaultRouter()
urlpatterns = router.urls + [
    path('example/ping', ping, name='ping'),
]
