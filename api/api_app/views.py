from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Stat, Player
from .serializers import StatSerializer

@api_view(["GET"])
def get_all(request, format=None):
    all_stats = Stat.objects.all()[:10]
    serializer = StatSerializer(all_stats, many=True)
    return Response(serializer.data, status=status.HTTP_302_FOUND)
