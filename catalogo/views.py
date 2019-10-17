from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

# Create your views here.

def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    #libros disponibles
    num_instances_avariable=BookInstance.objects.filter(status__exact='a').count() #en clase models
    num_authors=Author.objects.count() #el all() esta implicito por defecto.

    #renderoza la plantilla html index.html con los datos en la variable contexto
    return render(    #reenvia la informacion
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,
        'num_instances_avariable':num_instances_avariable,'num_authors':num_authors},
    )
