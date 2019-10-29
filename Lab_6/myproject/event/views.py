from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
users = ["user 1 data", "user 2 data", "user 3 data"]
events = ["1 event data", "2 event data", "3 event data"]


@api_view(['GET','POST'])
def get(request):
    if request.method == 'GET':
        return Response(users)
    elif request.method == 'POST':
        users.append("This is new user")
        return Response(users)


@api_view(['GET'])
def getUser(request, id):
    if request.method == 'GET':
        return Response(users[int(id)])


@api_view(['GET','POST'])
def getEvents(request):
    if request.method == 'GET':
        return Response(events)
    elif request.method == 'POST':
        users.append("This is new event")
        return Response(events)


@api_view(['GET'])
def getEvent(request, id):
    if request.method == 'GET':
        return Response(events[int(id)])
