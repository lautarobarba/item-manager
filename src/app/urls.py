from django.urls import path
from app.views import (
    IndexView,
    DashboardView,
    UsuarioListView, UsuarioCreateView, UsuarioDetailView, UsuarioUpdateView,UsuarioDeleteView,
    ProyectoListView, ProyectoCreateView, ProyectoDetailView, ProyectoUpdateView, ProyectoDeleteView,
    EstadoItemListView, EstadoItemCreateView
)

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    #Urls para los usuarios
    path('usuario/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuario/create/', UsuarioCreateView.as_view(), name='usuario-create'),
    path('usuario/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),
    path('usuario/update/<int:pk>/', UsuarioUpdateView.as_view(), name='usuario-update'),
    path('usuario/delete/<int:pk>/', UsuarioDeleteView.as_view(), name='usuario-delete'),

    #Urls para los proyectos
    path('proyecto/', ProyectoListView.as_view(), name='proyecto-list'),
    path('proyecto/create/', ProyectoCreateView.as_view(), name='proyecto-create'),
    path('proyecto/<int:pk>/', ProyectoDetailView.as_view(), name='proyecto-detail'),
    path('proyecto/update/<int:pk>/', ProyectoUpdateView.as_view(), name='proyecto-update'),
    path('proyecto/delete/<int:pk>/', ProyectoDeleteView.as_view(), name='proyecto-delete'),
    
    
    
    
    #######################

    #Urls para los estados de items
    path('estadoitem/', EstadoItemListView.as_view(), name='estadoitem-list'),
    path('estadoitem/<int:pk>/', EstadoItemListView.as_view(), name='estadoitem-detail'),
    path('estadoitem/create/', EstadoItemCreateView.as_view(), name='estadoitem-create'),
]
