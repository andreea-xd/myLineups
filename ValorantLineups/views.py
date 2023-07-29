import app as app
from django.contrib.auth.decorators import login_required
from django.views import View
from flask import Flask, render_template
import django_filters
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.contrib.auth.models import User

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from ValorantLineups.forms import UserForm, ContactRequestForm
from ValorantLineups.models import *


class AgentsList(ListView):
    model = Agent
    context_object_name = 'agents'
    template_name = 'agents_list.html'
    queryset = Agent.objects.all()


class AbilityList(ListView):
    model = Ability
    context_object_name = 'abilities'
    template_name = 'home.html'
    queryset = Ability.objects.all()


class MapList(ListView):
    model = Map
    context_object_name = 'maps'
    queryset = Map.objects.all()


class VideoList(ListView):
    model = Video
    context_object_name = 'videos'
    template_name = 'video_list.html'
    queryset = Video.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        print(self.request.GET)
        map_id = self.request.GET.get('map_id')
        agent_id = self.request.GET.get('agent_id')
        ability_id = self.request.GET.get('ability_id')
        side = self.request.GET.get('side')
        type = self.request.GET.get('type')
        videos = Video.objects.filter(map_id=map_id, agent_id=agent_id, ability_id=ability_id, type=type, part=side)
        print(f'videos={videos}')
        context[self.context_object_name] = videos
        context['maps'] = Map.objects.all().order_by('name')
        context['agents'] = Agent.objects.all().order_by('name')
        context['abilities'] = Ability.objects.all().order_by('name')
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


#
#
# class UserUpdateView(UpdateView):
#     model = User
#     form_class = UserUpdateForm
#     template_name = 'user_profile.html'
#
#     def get_success_url(self):
#         return reverse_lazy('update_profile', kwargs={'pk': self.request.user.id})


class Contact(CreateView):
    model = ContactRequest
    form_class = ContactRequestForm
    template_name = 'contact.html'
    success_url = reverse_lazy('home')


class FavoriteVideosView(ListView):
    model = FavoritesVideo
    template_name = 'favorite_videos.html'

    # def get_queryset(self):
    #     return Video.objects.filter(favorite__user=self.request.user)

    # @login_required
    # def favorite_videos(self):
    #     videos = Video.objects.filter(favorite__user=self.user)
    #     context = {'videos': videos}
    #     return render(self, 'favorite_videos.html', context)
