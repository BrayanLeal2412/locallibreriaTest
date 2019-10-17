from django.urls import path
from . import views
urlpatterns = [ 
      #llamada al metodo index creado en views
     path('',views.index,name='index'),
]