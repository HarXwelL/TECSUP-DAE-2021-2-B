from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('libros', views.libros),
    path('usuarios', views.usuarios),
    path('prestamos', views.prestamos),
    path('autor', views.autor),
    path('prestamos/<int:prestamos_id>', views.prestamodetalle)
]
