from app.models import CambioEstado
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class CambioEstadoCreatePopupView(LoginRequiredMixin, CreateView):
    model = CambioEstado
    template_name = 'app/cambio_estado_create_popup.html'
    fields = '__all__'
    success_url = reverse_lazy('created')