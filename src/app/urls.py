"""item_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app.views import (
    IndexView,
    DashboardView,
    UsuarioListView, UsuarioCreateView, UsuarioDeleteView
)

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    #Urls de usuarios
    path('usuario/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuario/create/', UsuarioCreateView.as_view(), name='usuario-create'),
    path('usuario/delete/<int:pk>/', UsuarioDeleteView.as_view(), name='usuario-delete'),
]
