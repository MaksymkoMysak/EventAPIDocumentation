from django.urls import path
from .views import UserList, UserView, EventsView, EventView, EventUsersView

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserView.as_view()),
    path('event/', EventsView.as_view()),
    path('event/<int:pk>/', EventView.as_view()),
    path('eventUsers/<event>', EventUsersView.as_view()),
]
