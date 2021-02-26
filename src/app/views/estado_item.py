from app.models import EstadoItem
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

class EstadoItemListView(LoginRequiredMixin, ListView):
    template_name = 'app/estado_item_list.html'
    model = EstadoItem
    queryset = EstadoItem.objects.order_by('nombre')

class EstadoItemCreateView(LoginRequiredMixin, CreateView):
    model = EstadoItem
    template_name = 'app/estado_item_create.html'
    fields = '__all__'

class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = EstadoItem
    template_name = 'app/usuario_delete.html'
    success_url = reverse_lazy('usuario-list')