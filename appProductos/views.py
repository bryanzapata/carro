from django.shortcuts import render
from .models import *


# Create your views here.
def verCategorias(request):
    listaCateg = Categoria.objects.all()

    context = {
        'categorias': listaCateg,
        'titulo': 'Categorias de Productos del supermercado'
    }

    return render(request, 'productos/categorias.html', context)

def verProductosCategoria(request, idCategoria):
#Consultar categorias
    idCat = int(idCategoria)
    nombreCat = Categoria.objects.get(id=idCat)
    listaProductos = Producto.objects.filter(categoria= idCat)
#ensamblar context
    context = {
    'productos': listaProductos,
    'titulo': 'Productos de la categoria ' + str(nombreCat),
}
#renderizar
    return render(request, 'productos/productos.html', context)

def verProductosCategoria(request, idCategoria):
#Consultar categorias
    idCat = int(idCategoria)
    nombreCat = Categoria.objects.get(id=idCat)
    listaProductos = Producto.objects.filter(categoria= idCat)
#ensamblar context
    context = {
        'productos': listaProductos,
        'titulo': 'Productos de la categoria ' + str(nombreCat),
}
#renderizar
    return render(request, 'productos/productos.html', context)