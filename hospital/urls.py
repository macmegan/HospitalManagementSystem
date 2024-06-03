"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from management.views import (
    GetRoomsView, 
    CreateUserView,
    GetAllUsersView,
    GetAllReservationsView,
    GetReservationsByUserView,
    CreateReservationView,
    RemoveReservationView,
    Home,
    AllUsers,
    AddUser,
    AllReservations,
    AllRooms,
    ReserveRoom,
    ReservationConfirmation
)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('all-users', AllUsers.as_view(), name='all-users'),
    path('add-user', AddUser.as_view(), name='add-user'),
    path('all-reservations', AllReservations.as_view(), name='all-reservations'),
    path('all-rooms', AllRooms.as_view(), name='all-rooms'),
    path('reserve-room', ReserveRoom.as_view(), name='reserve-room'),
    path('reservation-confirmation', ReservationConfirmation.as_view(), name='reservation-confirmation'),
    path('api/rooms', GetRoomsView.as_view(), name='rooms'),
    path('api/users', GetAllUsersView.as_view(), name='users'),
    path('api/reservations', GetAllReservationsView.as_view(), name='reservations'),
    path('api/reservations/<int:user_id>/', GetReservationsByUserView.as_view(), name='reservations-by-user-id'),
    path('api/create-user', CreateUserView.as_view(), name='create-user'),
    path('api/create-reservation', CreateReservationView.as_view(), name='create-reservation'),
    path('api/remove-reservation/<int:reservation_id>/', RemoveReservationView.as_view(), name='remove-reservation'),
]
