import random
import string

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from rest_framework.views import APIView

from .models import Room, User, Reservation
from .serializers import RoomSerializer, ReservationSerializer, UserSerializer

class GetRoomsView(APIView):
    def get(self, request):
        serializer = RoomSerializer(Room.objects.all(), many=True)

        return JsonResponse(serializer.data, safe=False, status=200)
    
class GetAllReservationsView(APIView):
    def get(self, request):
        serializer = ReservationSerializer(Reservation.objects.all(), many=True)

        return JsonResponse(serializer.data, safe=False, status=200)
    
class GetReservationsByUserView(APIView):
    def get(self, request, user_id):
        serializer = ReservationSerializer(Reservation.objects.filter(user_id=user_id), many=True)

        return JsonResponse(serializer.data, safe=False, status=200)
    
class GetAllUsersView(APIView):
    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)

        return JsonResponse(serializer.data, safe=False, status=200)
    
class CreateUserView(APIView):
    def post(self, request):
        email = request.data['email']
        name = request.data['name']

        user = User.objects.create(
            email=email, 
            name=name,
            username=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
        )

        return HttpResponseRedirect('/')
    
class CreateReservationView(APIView):
    def post(self, request):
        room_id = request.data['room_id']
        user_id = request.data['user_id']

        reservation = Reservation.objects.create(
            room_id=room_id, 
            user_id=user_id,
        )

        room = Room.objects.get(pk=room_id)
        room.capacity -= 1
        room.save()

        user = User.objects.get(pk=user_id)


        return render(request, template_name='reservation_confirmation.html', context={'user': user, 'room': room})
    
class RemoveReservationView(APIView):
    def get(self, request, reservation_id):
        reservation = Reservation.objects.get(pk=reservation_id)

        room = Room.objects.get(pk=reservation.room_id)
        room.capacity += 1
        room.save()

        reservation.delete()

        return render(request, template_name='reservation_view.html', context={'reservations': Reservation.objects.all()})
        

    def delete(self, request, reservation_id):
        return JsonResponse({}, status=200)
    
class Home(TemplateView):
    template_name = 'admin_portal.html'

class AllUsers(TemplateView):
    template_name = 'user_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        return context

class AddUser(TemplateView):
    template_name = 'new_user.html'

class AllReservations(TemplateView):
    template_name = 'reservation_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservations"] = Reservation.objects.all()
        return context
    
class AllRooms(TemplateView):
    template_name = 'rooms_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = Room.objects.all()
        return context
    
class ReserveRoom(TemplateView):
    template_name = 'reserve_room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = Room.objects.all()
        context["users"] = User.objects.all()
        return context
    
class ReservationConfirmation(TemplateView):
    template_name = 'reservation_confirmation.html'
