from django.urls import path, include

from . import views

urlpatterns = [
    path('base', views.base, name = 'base'),
    path('tipo_parlante', views.tipo_parlante, name='tipo_parlante'),
    path('menu', views.menu, name='menu'),
    path('agregar', views.agregar, name='agregar'),
    path('agregar_parlante', views.agregar_parlante, name='agregar_parlante'),
    path('boton_buscar', views.boton_buscar, name='boton_buscar'),
    path('buscar_por_nombre', views.buscar_por_nombre, name='buscar_por_nombre'),
    path('eliminar', views.eliminar, name='eliminar'),
    path('eliminar_por_nombre', views.eliminar_por_nombre, name='eliminar_por_nombre'),
    path('editar', views.editar, name='editar'),
    path('editar_por_nombre', views.editar_por_nombre, name='editar_por_nombre'),
    path('actualizar_parlante', views.actualizar_parlante, name='actualizar_parlante'),
    path('listar', views.listar, name='listar'),
    path('mostrar_parlantes', views.mostrar_parlantes, name='mostrar_parlantes'),
]
