from app.models import CambioEstado
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

class CambioEstadoCreatePopupView(LoginRequiredMixin, CreateView):
    model = CambioEstado
    template_name = 'app/cambio_estado_create_popup.html'
    fields = '__all__'

    #def post(self, request, *args, **kwargs):

        #form = self.form_class(request.POST)
        #if form.is_valid():
            #new_user = form.save()
            #new_user.set_password(form.cleaned_data['password1'])
            #new_user.save()
            #return redirect('created')
        #else:
            #return render(request, 'app/usuario_create.html', {'form': form})