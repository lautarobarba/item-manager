from django.urls import path
from app.views import (
    IndexView,
    DashboardView,
    CreatedView,
    UsuarioListView, UsuarioCreateView, UsuarioDetailView, UsuarioUpdateView,UsuarioDeleteView, UsuarioCreatePopupView,
    ProyectoListView, ProyectoCreateView, ProyectoDetailView, ProyectoUpdateView, ProyectoDeleteView,
    EstadoItemListView, EstadoItemCreateView, EstadoItemDetailView, EstadoItemUpdateView,EstadoItemDeleteView,

)

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    #Url creacion de objetos desde popup 
    path('created/', CreatedView.as_view(), name='created'),

    #Urls para los usuarios
    path('usuario/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuario/create/', UsuarioCreateView.as_view(), name='usuario-create'),
    path('usuario/create/popup/', UsuarioCreatePopupView.as_view(), name='usuario-create-popup'),
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
    path('estadoitem/create/', EstadoItemCreateView.as_view(), name='estadoitem-create'),
    # FALTA CREATE POPUP
    path('estadoitem/<int:pk>/', EstadoItemDetailView.as_view(), name='estadoitem-detail'),
    path('estadoitem/update/<int:pk>/', EstadoItemUpdateView.as_view(), name='estadoitem-update'),
    path('estadoitem/delete/<int:pk>/', EstadoItemDeleteView.as_view(), name='estadoitem-delete'),

    #Urls para los tipos de items
    path('estadoitem/', EstadoItemListView.as_view(), name='estadoitem-list'),
    path('estadoitem/create/', EstadoItemCreateView.as_view(), name='estadoitem-create'),
    # FALTA CREATE POPUP
    path('estadoitem/<int:pk>/', EstadoItemDetailView.as_view(), name='estadoitem-detail'),
    path('estadoitem/update/<int:pk>/', EstadoItemUpdateView.as_view(), name='estadoitem-update'),
    path('estadoitem/delete/<int:pk>/', EstadoItemDeleteView.as_view(), name='estadoitem-delete'),
]
