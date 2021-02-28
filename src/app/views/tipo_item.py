from app.models import TipoItem
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from django.db.models import ProtectedError
from django.urls import reverse_lazy

class TipoItemListView(LoginRequiredMixin, ListView):
    template_name = 'app/tipo_item_list.html'
    model = TipoItem
    queryset = TipoItem.objects.order_by('nombre')

class TipoItemCreateView(LoginRequiredMixin, CreateView):
    model = TipoItem
    template_name = 'app/tipo_item_create.html'
    fields = '__all__'

class TipoItemDetailView(LoginRequiredMixin, DetailView):
    model = TipoItem
    template_name = 'app/tipo_item_detail.html'

class TipoItemUpdateView(LoginRequiredMixin, UpdateView):
    model = TipoItem
    template_name = 'app/tipo_item_update.html'
    fields = '__all__'

class TipoItemDeleteView(LoginRequiredMixin, DeleteView):
    model = TipoItem
    template_name = 'app/tipo_item_delete.html'
    success_url = reverse_lazy('tipoitem-list')

    def post(self, request, *args, **kwargs):
        objeto = self.model.objects.get(pk=kwargs['pk'])
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            return render(request, 'app/error_protected.html', {'objeto': objeto})