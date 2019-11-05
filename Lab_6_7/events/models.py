from django.db import models


class User(models.Model):
    userName = models.CharField(max_length=250)
    numOfCreatedEvents = models.IntegerField(default=0)
    numOfParticipatingEvents = models.IntegerField(default=0)

    def __str__(self):
        return self.userName


class Event(models.Model):
    eventName = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.IntegerField(default=0)
    location = models.CharField(max_length=250)
    numOfParticipants = models.IntegerField(default=0)

    def __str__(self):
        return self.eventName
