from rest_framework import serializers
from events import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'userName',
            'numOfCreatedEvents',
            'numOfParticipatingEvents',
        )
        # fields = '_all_'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = (
            'eventName',
            'user',
            'date',
            'location',
            'numOfParticipants',
        )
