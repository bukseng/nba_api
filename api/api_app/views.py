from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Stats
from .serializers import StatsSerializer

@api_view(["GET"])
def get_all(request, format=None):
    all_stats = Stats.objects.all()
    serializer = StatsSerializer(all_stats, many=True)
    return Response(serializer.data, status=status.HTTP_302_FOUND)
