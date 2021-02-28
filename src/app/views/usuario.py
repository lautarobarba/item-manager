from django.contrib.auth.models import User
from app.forms import UserCreationForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from django.db.models import ProtectedError
from django.urls import reverse_lazy

class UsuarioListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'app/usuario_list.html'
    queryset = User.objects.order_by('username')

class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'app/usuario_create.html'

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            return redirect('usuario-list')
        else:
            return render(request, 'app/usuario_create.html', {'form': form})

class UsuarioCreatePopupView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'app/usuario_create_popup.html'

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            return redirect('created')
        else:
            return render(request, 'app/usuario_create.html', {'form': form})

class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'app/usuario_detail.html'

class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'app/usuario_update.html'
    success_url = reverse_lazy('usuario-list')

class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'app/usuario_delete.html'
    success_url = reverse_lazy('usuario-list')

    def post(self, request, *args, **kwargs):
        objeto = self.model.objects.get(pk=kwargs['pk'])
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            return render(request, 'app/error_protected.html', {'objeto': objeto})