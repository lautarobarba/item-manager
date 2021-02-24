from django.contrib.auth.models import User
from app.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

class UsuarioListView(LoginRequiredMixin, ListView):
    template_name = 'app/usuario_list.html'
    model = User
    queryset = User.objects.order_by('username')

class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'app/usuario_create.html'
    form_class = UserCreationForm

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            return redirect('usuario-list')
        else:
            return render(request, 'app/usuario_create.html', {'form': form})

class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'app/usuario_delete.html'
    success_url = reverse_lazy('usuario-list')