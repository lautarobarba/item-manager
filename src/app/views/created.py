from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class CreatedView(LoginRequiredMixin, TemplateView):
    template_name = 'app/created.html'