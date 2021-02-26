from app.models import Proyecto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.shortcuts import render


class ProyectoListView(LoginRequiredMixin, ListView):
    template_name = 'app/proyecto_list.html'
    model = Proyecto
    queryset = Proyecto.objects.order_by('nombre')

class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    template_name = 'app/proyecto_create.html'
    fields = '__all__'

class ProyectoDetailView(LoginRequiredMixin, DetailView):
    model = Proyecto
    template_name = 'app/proyecto_detail.html'

class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    template_name = 'app/proyecto_update.html'
    fields = '__all__'

class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = 'app/proyecto_delete.html'
    success_url = reverse_lazy('proyecto-list')

    def post(self, request, *args, **kwargs):
        objeto = self.model.objects.get(pk=kwargs['pk'])
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            return render(request, 'app/error_protected.html', {'objeto': objeto})