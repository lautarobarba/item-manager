from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

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