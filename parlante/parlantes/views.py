from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from parlantes.models import Parlante

def base(requeest):
    print("Estamos en la vista base..")
    context = {}
    return render(requeest, 'parlantes/base.html', context)

#decorador
@login_required
def menu(requeest):
    print("Estamos en la vista menu..")
    context = {}
    return render(requeest, 'parlantes/index.html', context)

#decorador
@login_required
def tipo_parlante(requeest):
    print("Estamos en la vista tipo parlante..")
    lista = Parlante.objects.all()
    context={'listado' : lista}
    return render(requeest, 'parlantes/tipoParlantes.html', context)

#decorador
@login_required
def agregar(request):
    print("ok, estamos en la vista agregarr")
    context={}
    return render(request, 'parlantes/crud/formulario_agregar.html', context)

#decorador
@login_required
def agregar_parlante(request):
    print("hola  estoy en agregar_parlante...")
    if request.method == 'POST':
       mi_codigo = request.POST['codigo']
       mi_nombre = request.POST['nombre']
       mi_tipo   = request.POST['tipo']
       mi_foto   = request.FILES['foto']

       if mi_nombre != "":
           if mi_tipo == 'bazucas' or mi_tipo == 'Karaoke' or mi_tipo == 'parlantes' or mi_tipo == "cubos" or mi_tipo == "deDJ":
               try:
                   parlante = Parlante()

                   parlante.codigo = mi_codigo
                   parlante.nombre = mi_nombre
                   parlante.tipo = mi_tipo
                   parlante.foto = mi_foto

                   parlante.save()

                   return render(request, 'parlantes/mensajes/datos_grabados.html', {})
               except parlante.DoesNotExist:
                   return render(request, 'parlantes/errores/error_204.html', {})
           else:
               return render(request, 'parlantes/errores/error_205.html', {})
       else:
           return render(request, 'parlantes/errores/error_201.html', {})
    else:
        return render(request, 'parlantes/errores/error_203.html', {})

#decorador
@login_required
def boton_buscar(request):
    print("ok, estamos en la vista boton buscar")
    context={}
    return render(request, 'parlantes/crud/boton_buscar.html', context)

#decorador
@login_required
def buscar_por_codigo(request):
    print("hola  estoy en buscar_por_codigo...")
    if request.method == 'POST':
       mi_codigo = request.POST['codigo']

       if mi_codigo != "":
           try:
               parlante = Parlante()
               parlante = Parlante.objects.get(codigo=mi_codigo)
               if parlante is not None:
                   print("Parlante=", parlante)
                   context={'parlante': parlante}
                   return render(request, 'parlantes/crud/mostrar_datos.html', context)
               else:
                   return render(request, 'parlantes/errores/error_202.html',{})
           except parlante.DoesNotExist:
               return render(request, 'parlantes/errores/error_202.html', {})
       else:
           return render(request, 'parlantes/errores/error_201.html', {})
    else:
        return render(request, 'parlantes/errores/error_203.html', {})

#decorador
@login_required
def eliminar(request):
    print("ok, estamos en la vista eliminar")
    context={}
    return render(request, 'parlantes/crud//boton_eliminar.html', context)

#decorador
@login_required
def eliminar_por_codigo(request):
    print("hola  estoy en eliminar_por_codigo...")
    if request.method == 'POST':
       mi_codigo = request.POST['codigo']

       if mi_codigo != "":
           try:
               parlante = Parlante()
               #parlante = Parlante.objects.all()
               parlante = Parlante.objects.get(codigo = mi_codigo)
               if parlante is not None:
                   print("Parlante=", parlante)
                   parlante.delete()
                   return render(request, 'parlantes/mensajes/parlante_eliminado.html', {})
               else:
                   return render(request, 'parlantes/errores/error_202.html',{})
           except parlante.DoesNotExist:
               return render(request, 'parlantes/errores/error_202.html', {})
       else:
           return render(request, 'parlantes/errores/error_201.html', {})
    else:
        return render(request, 'parlantes/errores/error_203.html', {})

#decorador
@login_required
def editar(request):
    print("ok, estamos en la vista editar")
    context = {}
    return render(request, 'parlantes/crud/boton_editar.html', context)

#decorador
@login_required
def editar_por_codigo(request):
    print("hola  estoy en editar_por_codigo...")
    if request.method == 'POST':
       mi_codigo = request.POST['codigo']

       if mi_codigo != "":
           try:
               parlante = Parlante()
               parlante = Parlante.objects.get(codigo = mi_codigo)
               if parlante is not None:
                   print("Parlante=", parlante)
                   context={'parlante': parlante}
                   return render(request, 'parlantes/crud/formulario_editar.html', context)
               else:
                   return render(request, 'parlantes/errores/error_202.html',{})
           except parlante.DoesNotExist:
               return render(request, 'parlantes/errores/error_202.html', {})
       else:
           return render(request, 'parlantes/errores/error_201.html', {})
    else:
        return render(request, 'parlantes/errores/error_203.html', {})

#decorador
@login_required
def actualizar_parlante(request):
    print("hola  estoy en actualizar_parlante...")
    if request.method == 'POST':

       mi_id     = request.POST['id_parlante']
       mi_codigp = request.POST['codigo']
       mi_nombre = request.POST['nombre']
       mi_tipo   = request.POST['tipo']
       mi_foto   = request.FILES['foto']

       if mi_nombre != "":
           if mi_tipo == 'bazucas' or mi_tipo == 'Karaoke' or mi_tipo == 'parlantes' or mi_tipo == "cubos" or mi_tipo == "deDJ":
               try:
                   parlante = Parlante()

                   parlante.id_parlante = mi_id
                   parlante.codigo = mi_codigp
                   parlante.nombre = mi_nombre
                   parlante.tipo = mi_tipo
                   parlante.foto = mi_foto

                   parlante.save()

                   return render(request, 'parlantes/mensajes/dato_editado.html',{})

               except parlante.DoesNotExist:
                   return render(request, 'parlantes/errores/error_204.html', {})
           else:
               return render(request, 'parlantes/errores/error_205.html', {})
       else:
           return render(request, 'parlantes/errores/error_201.html', {})
    else:
        return render(request, 'parlantes/errores/error_203.html', {})

def listar(request):
    print("ok, estamos en la vista listar")
    context={}
    return render(request, 'parlantes/crud/listar.html', context)

def mostrar_parlantes(request):
    print("ok, estamos en la vista mostrar parlantes")
    #lista = Parlante.objects.all()
    lista = Parlante.objects.filter(tipo = 'bazucas')
    context={'listado' : lista}
    return render(request, 'parlantes/crud/listar_parlantes.html', context)