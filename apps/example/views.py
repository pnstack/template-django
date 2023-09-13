from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework_nested import routers
from django.urls import path
from rest_framework.response import Response

@api_view()
def ping(request):
    return Response("pong")


