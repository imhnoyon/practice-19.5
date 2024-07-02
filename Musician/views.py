from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from . import models
from . import forms
from Album.models import AlbumModel
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class MusicianCreateview(LoginRequiredMixin,CreateView):
    model=models.MusicianModel
    form_class=forms.MusicianForm
    template_name='Musician_form.html'
    success_url = reverse_lazy('musician')

class MusicianUpdateView(LoginRequiredMixin,UpdateView):
    model = models.MusicianModel
    form_class = forms.MusicianForm
    pk_url_kwarg='id'
    template_name = 'Musician_form.html'
    success_url = reverse_lazy('listview')


class MusicianDeleteView(LoginRequiredMixin,DeleteView):
    model = models.MusicianModel
    success_url = reverse_lazy('listview')


class listview(ListView):
    model=AlbumModel
    template_name='list_view.html'
    context_object_name = 'Albums'