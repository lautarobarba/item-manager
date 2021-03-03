from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from app.models import Item
from django.views.generic.edit import UpdateView
from app.models import Snapshot
from app.forms import ItemUpdateEstadoForm
from django.shortcuts import redirect

class MisProyectosListView(LoginRequiredMixin, TemplateView):
    template_name = 'app/mis_proyectos_list.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        self.proyectos_liderados = user.lidera.all
        self.proyectos_participados = user.participa.all
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyectos_liderados'] = self.proyectos_liderados
        context['proyectos_participados'] = self.proyectos_participados
        return context
    
class MisItemsListView(LoginRequiredMixin, TemplateView):
    template_name = 'app/mis_items_list.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        self.items_controlados = user.controla.all
        self.items_trabajados = user.trabaja.all
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items_controlados'] = self.items_controlados
        context['items_trabajados'] = self.items_trabajados
        return context

class ItemUpdateResponsableView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = 'app/item_update_responsable.html'
    fields = ['responsable']

    def post(self, request, *args, **kwargs):
        # Item antes de actualizar
        item = Item.objects.get(pk=kwargs['pk'])
        responsable_viejo = item.responsable.id

        # El item actualizado
        super().post(request, *args, **kwargs)
        item = Item.objects.get(pk=kwargs['pk'])
        responsable_nuevo = item.responsable.id

        if responsable_nuevo != responsable_viejo:
            # Snapshot que corresponde al nuevo cambio
            sanpshot = Snapshot(item=item, estado=item.estado, responsable=item.responsable)
            sanpshot.save()

        return super().post(request, *args, **kwargs)

class ItemUpdateEstadoView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemUpdateEstadoForm
    template_name = 'app/item_update_estado.html'

    def post(self, request, *args, **kwargs):

        # Item antes de actualizar
        pk = kwargs['pk']
        item = Item.objects.get(pk=pk)
        estado_viejo = item.estado

        super().post(request, *args, **kwargs)
        item = Item.objects.get(pk=kwargs['pk'])
        estado_nuevo = item.estado

        if estado_viejo != estado_nuevo:
            # Snapshot que corresponde al nuevo cambio
            sanpshot = Snapshot(item=item, estado=item.estado, responsable=item.responsable)
            sanpshot.save()

        return redirect('item-detail', pk=pk)