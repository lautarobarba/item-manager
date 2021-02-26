from django.urls import path
from app.views import (
    IndexView,
    DashboardView,
    UsuarioListView, UsuarioCreateView, UsuarioUpdateView,UsuarioDeleteView,
    EstadoItemListView, EstadoItemCreateView
)

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    #Urls para los usuarios
    path('usuario/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuario/create/', UsuarioCreateView.as_view(), name='usuario-create'),
    path('usuario/update/<int:pk>/', UsuarioUpdateView.as_view(), name='usuario-update'),
    path('usuario/delete/<int:pk>/', UsuarioDeleteView.as_view(), name='usuario-delete'),

    #Urls para los estados de items
    path('estadoitem/', EstadoItemListView.as_view(), name='estadoitem-list'),
    path('estadoitem/<int:pk>/', EstadoItemListView.as_view(), name='estadoitem-detail'),
    path('estadoitem/create/', EstadoItemCreateView.as_view(), name='estadoitem-create'),
]
