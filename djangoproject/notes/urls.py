from django.urls import path
from .views import lista_notas, crear_nota, editar_nota, eliminar_nota

urlpatterns = [
    path('', lista_notas, name='lista_notas'),
    path('crear/', crear_nota, name='crear_nota'),
    path('editar/<int:pk>/', editar_nota, name='editar_nota'),
    path('eliminar/<int:pk>/', eliminar_nota, name='eliminar_nota'),
]

