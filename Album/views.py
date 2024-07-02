from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView
from . import models
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AlbumCreateView(LoginRequiredMixin,CreateView):
    model=models.AlbumModel
    form_class =forms.AlbumForm
    template_name='Album_form.html'
    success_url = reverse_lazy('CrateAlbum')


class EditAlbum(LoginRequiredMixin,UpdateView):
    model=models.AlbumModel
    form_class=forms.AlbumForm
    pk_url_kwarg='id'
    template_name='Album_form.html'
    success_url = reverse_lazy('CreateAlbum')
    
class DeleteAlbum(DeleteView):
    model=models.AlbumModel
    pk_url_kwarg='id'
    template_name='delete_form.html'
    success_url = reverse_lazy('listview')


    