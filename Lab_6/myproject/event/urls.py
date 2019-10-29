from django.urls import path
from .views import get
from .views import getUser
from .views import getEvent
from .views import getEvents
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('user/', get),
    path('user/<id>/', getUser),
    path('events/', getEvents),
    path('event/<id>/', getEvent),
]