from django.urls import path
from . import views
from .views import ListaAnunciosView, CargaPaginaAnuncioView, NuevoAnuncioView, EliminarAnuncioView, EditarAnuncioView

app_name = "anuncios"

urlpatterns = [
    # Funcion vs Clase
    # path('', views.lista_anuncios, name="listar"),
    path('', ListaAnunciosView.as_view(), name='listar'),

    # Solo Funcion
    path('otrolistar', views.otra_lista_anuncios, name="otrolistar"),

    # Funcion vs Clase para creacion de nuevo anuncio, detall, edicion y eliminacion
    # path('nuevo_anuncio', views.nuevo_anuncio, name="nuevo_anuncio"),
    path('nuevo_anuncio/', NuevoAnuncioView.as_view(), name='nuevo_anuncio'),
    # path('<slug:slug>', views.pagina_anuncio, name="detalle"),
    path('<slug:slug>/', CargaPaginaAnuncioView.as_view(), name='detalle'),
    # path('editar_anuncio/<int:id>/', views.editar_anuncio, name="editar_anuncio"),
    path('editar_anuncio/<int:pk>/',
         EditarAnuncioView.as_view(), name='editar_anuncio'),
    # path('eliminar_anuncio/<int:id>/',views.eliminar_anuncio, name="eliminar_anuncio")
    path('eliminar_anuncio/<int:pk>/',
         EliminarAnuncioView.as_view(), name='eliminar_anuncio'),

    # Edicion custom la mantengo como funcion
    path('editar_anuncio_custom/<int:id>/',
         views.editar_anuncio_custom, name="editar_anuncio_custom"),
]
