from django.shortcuts import render,get_object_or_404
from .models import Categoria,Producto


def lista(request):
    listas = Producto.objects.all()
    category = Categoria.objects.all()
    return render(request, 'noticia/lista.html', {'listas': listas, 'category': category})

# Vista para filtrar productos por categoría
def category(request, category_id):
    categoria=get_object_or_404(Categoria, id=category_id)
    #categoria = Categoria.objects.get(id=category_id)  
    listas = Producto.objects.filter(category=categoria)  
    return render(request, 'noticia/category.html', {'listas': listas, 'categoria': categoria})