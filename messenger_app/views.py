from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Room, Message, User
from .forms import CreateRoomForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import UpdateView
from .models import User
from .forms import UserChangeForm

class ProfileUpdateView(UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'profile.html'
    success_url = '/'

    def get_object(self):
        return self.request.user


class HomeListView(ListView):
    model = Room
    template_name = 'home.html'
    context_object_name = 'rooms'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

class CreateRoomCreateView(CreateView):
    model = Room
    form_class = CreateRoomForm
    template_name = 'create_room.html'
    success_url = '/'

    def form_valid(self, form):
        room = form.save(commit=False)
        room.save()
        if self.request.user.is_authenticated:
            room.users.add(self.request.user)  # Добавление пользователя только если он аутентифицирован
        return super().form_valid(form)
    
    
from django.views.generic import DetailView
from django.shortcuts import redirect
from .models import Room, Message

class RoomDetailView(DetailView):
    model = Room
    template_name = 'room.html'
    context_object_name = 'room'

    def post(self, request, *args, **kwargs):
        room = self.get_object()
        message_text = request.POST.get('message')
        if message_text:
            user = request.user if request.user.is_authenticated else None
            Message.objects.create(room=room, user=user, text=message_text)
        return redirect('room', pk=room.pk)