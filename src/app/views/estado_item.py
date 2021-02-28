from app.models import EstadoItem
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from django.db.models import ProtectedError
from django.urls import reverse_lazy

class EstadoItemListView(LoginRequiredMixin, ListView):
    template_name = 'app/estado_item_list.html'
    model = EstadoItem
    queryset = EstadoItem.objects.order_by('nombre')

class EstadoItemCreateView(LoginRequiredMixin, CreateView):
    model = EstadoItem
    template_name = 'app/estado_item_create.html'
    fields = '__all__'

class EstadoItemCreatePopupView(LoginRequiredMixin, CreateView):
    model = EstadoItem
    template_name = 'app/estado_item_create_popup.html'
    fields = '__all__'
    success_url = reverse_lazy('created')

class EstadoItemDetailView(LoginRequiredMixin, DetailView):
    model = EstadoItem
    template_name = 'app/estado_item_detail.html'

class EstadoItemUpdateView(LoginRequiredMixin, UpdateView):
    model = EstadoItem
    template_name = 'app/estado_item_update.html'
    fields = '__all__'

class EstadoItemDeleteView(LoginRequiredMixin, DeleteView):
    model = EstadoItem
    template_name = 'app/estado_item_delete.html'
    success_url = reverse_lazy('estadoitem-list')

    def post(self, request, *args, **kwargs):
        objeto = self.model.objects.get(pk=kwargs['pk'])
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            return render(request, 'app/error_protected.html', {'objeto': objeto})