from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from events import models
from .serializers import UserSerializer
from events import serializers
from rest_framework import generics


# /user/
class UserList(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def get(self, request):
        queryset = self.get_queryset()
        serializer = serializers.UserSerializer(queryset, many=True)
        return Response(serializer.data)


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class EventsView(generics.ListCreateAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


class EventView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


class EventUsersView(generics.ListAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        ev = self.kwargs['event']
        return models.User.objects.filter(event=ev)