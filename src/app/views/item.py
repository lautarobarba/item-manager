from app.models import Item
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.shortcuts import render


class ItemListView(LoginRequiredMixin, ListView):
    template_name = 'app/item_list.html'
    model = Item
    queryset = Item.objects.order_by('nombre')

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = 'app/item_create.html'
    fields = '__all__'

class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = 'app/item_detail.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        item = Item.objects.get(pk=kwargs['pk'])
        autorizados = []
        autorizados.append(item.responsable.pk)
        for p in item.desarrolladores.all():
            autorizados.append(p.pk)
        #print(f'Id\'S Autorizados: {autorizados}')
        self.autorizados = autorizados
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autorizados'] = self.autorizados
        return context

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = 'app/item_update.html'
    fields = '__all__'

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = 'app/item_delete.html'
    success_url = reverse_lazy('item-list')

    def post(self, request, *args, **kwargs):
        objeto = self.model.objects.get(pk=kwargs['pk'])
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            return render(request, 'app/error_protected.html', {'objeto': objeto})