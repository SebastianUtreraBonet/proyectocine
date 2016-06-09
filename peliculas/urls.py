from django.conf.urls import url
from django.conf import settings
from . import views

from django.views.static import serve


urlpatterns = [
    url(r'^$', views.index, name='inicio'),
    url(r'^alfabetico', views.ord_alfabetico, name='peliculas.alfabetico'),
    url(r'^recientes', views.ord_fecha, name='peliculas.recientes'),
    url(r'^ficha', views.ficha),
    url(r'^genero', views.genero),
    url(r'actores$', views.veractores, name='peliculas.actores'),
    url(r'directores$', views.verdirectores, name='peliculas.directores'),
    url(r'^actor/', views.actor),
    url(r'^director/', views.director),
    url(r'^productora', views.productora),
    url(r'^buscar', views.buscar, name='buscar'),




    #formularios
    url(r'^agregar-pelicula/$', views.insertarpelicula, name='insertarpelicula'),
    url(r'^agregar-actor/$', views.insertaractor, name='insertaractor'),
    url(r'^agregar-director/$', views.insertardirector, name='insertardirector'),
    url(r'^agregar-genero/$', views.insertargenero, name='insertargenero'),
    url(r'^agregar-pais/$', views.insertarpais, name='insertarpais'),
    url(r'^agregar-productora/$', views.insertarproductora, name='insertarproductora'),


    #media (archivos de fotos)
    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    }),
]