from django.urls import path
from app.views import (
    IndexView,
    DashboardView,
    CreatedView,
    UsuarioListView, UsuarioCreateView, UsuarioDetailView, UsuarioUpdateView,UsuarioDeleteView, UsuarioCreatePopupView,
    ProyectoListView, ProyectoCreateView, ProyectoDetailView, ProyectoUpdateView, ProyectoDeleteView,
    EstadoItemListView, EstadoItemCreateView, EstadoItemDetailView, EstadoItemUpdateView,EstadoItemDeleteView, EstadoItemCreatePopupView,
    TipoItemListView, TipoItemCreateView, TipoItemDetailView, TipoItemUpdateView, TipoItemDeleteView,
    CambioEstadoCreatePopupView,
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
    path('estadoitem/create/popup/', EstadoItemCreatePopupView.as_view(), name='estadoitem-create-popup'),
    path('estadoitem/<int:pk>/', EstadoItemDetailView.as_view(), name='estadoitem-detail'),
    path('estadoitem/update/<int:pk>/', EstadoItemUpdateView.as_view(), name='estadoitem-update'),
    path('estadoitem/delete/<int:pk>/', EstadoItemDeleteView.as_view(), name='estadoitem-delete'),

    #Urls para los cambios de estado
    path('cambioestado/create/popup/', CambioEstadoCreatePopupView.as_view(), name='cambioestado-create-popup'),

    #Urls para los tipos de items
    path('tipoitem/', TipoItemListView.as_view(), name='tipoitem-list'),
    path('tipoitem/create/', TipoItemCreateView.as_view(), name='tipoitem-create'),
    # FALTA CREATE POPUP
    path('tipoitem/<int:pk>/', TipoItemDetailView.as_view(), name='tipoitem-detail'),
    path('tipoitem/update/<int:pk>/', TipoItemUpdateView.as_view(), name='tipoitem-update'),
    path('tipoitem/delete/<int:pk>/', TipoItemDeleteView.as_view(), name='tipoitem-delete'),


    #Urls para los items
    path('item/', .as_view(), name='item-list'),
    #path('item/create/', .as_view(), name='item-create'),
    #path('item/<int:pk>/', .as_view(), name='item-detail'),
    #path('item/update/<int:pk>/', .as_view(), name='item-update'),
    #path('item/delete/<int:pk>/', .as_view(), name='item-delete'),
]
