from django.urls import path, include

from . import views

urlpatterns = [
    path('base', views.base, name = 'base'),
    path('tipo_parlante', views.tipo_parlante, name='tipo_parlante'),
    path('menu', views.menu, name='menu'),
    path('agregar', views.agregar, name='agregar'),
    path('agregar_parlante', views.agregar_parlante, name='agregar_parlante'),
    path('boton_buscar', views.boton_buscar, name='boton_buscar'),
    path('buscar_por_codigo', views.buscar_por_codigo, name='buscar_por_codigo'),
    path('eliminar', views.eliminar, name='eliminar'),
    path('eliminar_por_codigo', views.eliminar_por_codigo, name='eliminar_por_codigo'),
    path('editar', views.editar, name='editar'),
    path('editar_por_codigo', views.editar_por_codigo, name='editar_por_codigo'),
    path('actualizar_parlante', views.actualizar_parlante, name='actualizar_parlante'),
    path('listar', views.listar, name='listar'),
    path('mostrar_parlantes', views.mostrar_parlantes, name='mostrar_parlantes'),
    path('api', views.api, name='api'),
]
