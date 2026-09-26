from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response


@extend_schema(responses=OpenApiTypes.STR)
@api_view()
def ping(request):
    return Response("pong")
