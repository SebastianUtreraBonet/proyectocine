from sys import path
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from django.template.defaulttags import ifequal

from .forms import *
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    peli = Peliculas.objects.all()
    return render(request, 'index.html', {'peli': peli[::-1]})

def ord_alfabetico(request):
    peli = Peliculas.objects.all().order_by('titulo')
    return render(request, 'index.html', {'peli': peli})

def ord_fecha(request):
    peli = Peliculas.objects.all().order_by('fecha_entrada')
    return render(request, 'index.html', {'peli': peli[::-1]})

def veractores(request):
    p = request.path;
    act = Actores.objects.all().order_by('nombre')
    return render(request, 'peliculas/buscador.html', {'mostrar1': act, 'p': p})

def verdirectores(request):
    p = request.path;
    dic = Directores.objects.all().order_by('nombre')
    return render(request, 'peliculas/buscador.html', {'mostrar2': dic, 'p': p})


def ficha(request):
    t = request.path[7::]
    ficha = Peliculas.objects.filter(titulo=t)
    act = Actores.objects.filter(peliculas__titulo=t).distinct()
    gen = Generos.objects.filter(peliculas__titulo=t).distinct()
    dis = Productoras.objects.filter(peliculas__titulo=t).distinct()
    return render(request, 'peliculas/ficha.html', {'ficha': ficha, 'act': act, 'gen': gen, 'dis': dis})

def genero(request):
    g = request.path[8::]
    genero = Peliculas.objects.filter(genero__genero=g).distinct()
    gen = Generos.objects.filter(genero=g).distinct()
    return render(request, 'peliculas/buscador.html', {'mostrar': genero, 'gen': gen})


def buscar(request):
    query = request.GET.get('buscar')
    if len(query) == 1:
        peli = Peliculas.objects.filter(titulo__startswith=query).order_by("titulo")
        act = Actores.objects.filter(nombre__startswith=query).order_by("nombre")
        dir = Directores.objects.filter(nombre__startswith=query).order_by("nombre")
        primeraLetra = 0
        if peli.count() + act.count() + dir.count() == 0:
            primeraLetra = 1
            peli = Peliculas.objects.filter(titulo__contains=query).order_by("titulo")
            act = Actores.objects.filter(nombre__contains=query).order_by("nombre")
            dir = Directores.objects.filter(nombre__contains=query).order_by("nombre")
    else:
        primeraLetra = 1
        peli = Peliculas.objects.filter(titulo__contains=query).order_by("titulo")
        act = Actores.objects.filter(nombre__contains=query).order_by("nombre")
        dir = Directores.objects.filter(nombre__contains=query).order_by("nombre")

    return render(request, "peliculas/buscador.html", {
        "mostrar": peli,
        "mostrar1": act,
        "mostrar2": dir,
        "pl":primeraLetra,
        "query": query,
    })


def actor(request):
    a = request.path[7::]
    actor = Peliculas.objects.filter(actores__nombre=a).distinct()
    pic = Actores.objects.filter(nombre=a)
    return render(request, 'peliculas/actores.html', {'actor': actor, 'pic': pic})


def director(request):
    d = request.path[10::]
    director = Peliculas.objects.filter(director__nombre=d).distinct()
    pic = Directores.objects.filter(nombre=d)
    return render(request, 'peliculas/directores.html', {'director': director, 'pic': pic})


def productora(request):
    p = request.path[12::]
    peliculas = Peliculas.objects.filter(productora__nombre=p).distinct()
    productora = Productoras.objects.filter(nombre=p).distinct()
    return render(request, 'peliculas/productoras.html', {'peliculas': peliculas, 'pro': productora})

@login_required
def insertarpelicula(request):
    if request.method == 'POST':
        form = AgregarPelicula(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            titulo = cleaned_data.get('titulo')
            caratula = cleaned_data.get('caratula')
            director = cleaned_data.get('director')
            actores = cleaned_data.get('actores')
            anio = cleaned_data.get('anio')
            sinopsis = cleaned_data.get('sinopsis')
            genero = cleaned_data.get('genero')
            pais = cleaned_data.get('pais')
            productora = cleaned_data.get('productora')
            pelicula_model = Peliculas.objects.create(titulo=titulo, caratula=caratula, director=director, anio=anio,
                                                      sinopsis=sinopsis, pais=pais, productora=productora)
            pelicula_model.actores = actores
            pelicula_model.genero = genero
            pelicula_model.save()
            return HttpResponseRedirect('../../')
    else:
        form = AgregarPelicula()
    context = {'form': form}
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'peliculas/insertar.html', context)

@login_required
def insertaractor(request):
    if request.method == 'POST':
        form = AgregarActor(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            nombre = cleaned_data.get('nombre')
            pais = cleaned_data.get('pais')
            fecha = cleaned_data.get('fecha')
            imagen = cleaned_data.get('imagen')
            actor_model = Actores.objects.create(nombre=nombre, pais=pais, fecha_nacimiento=fecha, foto=imagen)
            actor_model.save()
            return render(request, "peliculas/cerrar.html")

    else:
        form = AgregarActor()
    context = {'form': form}
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, "peliculas/insertar2.html", context)

@login_required
def insertardirector(request):
    if request.method == 'POST':
        form = AgregarDirector(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            nombre = cleaned_data.get('nombre')
            pais = cleaned_data.get('pais')
            fecha = cleaned_data.get('fecha')
            imagen = cleaned_data.get('imagen')
            director_model = Directores.objects.create(nombre=nombre, pais=pais, fecha_nacimiento=fecha, foto=imagen)
            director_model.save()
            return render(request, 'peliculas/cerrar.html')
    else:
        form = AgregarDirector()
    context = {'form': form}
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, "peliculas/insertar2.html", context)


def insertargenero(request):
    if request.method == 'POST':
        form = AgregarGenero(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            genero = cleaned_data.get('genero')
            genero_model = Generos.objects.create(genero=genero)
            genero_model.save()
            return render(request, 'peliculas/cerrar.html')
    else:
        form = AgregarGenero()
    context = {'form': form}
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, "peliculas/insertar2.html", context)


def insertarpais(request):
    if request.method == 'POST':
        form = AgregarPais(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            nombre = cleaned_data.get('nombre')
            bandera = cleaned_data.get('bandera')
            pais_model = Paises.objects.create(nombre=nombre, bandera=bandera)
            pais_model.save()
            return render(request, 'peliculas/cerrar.html')

    else:
        form = AgregarPais()
    context = {'form': form}
    """args={}
    args.update(csrf(request))
    args['form']=form"""
    return render(request, 'peliculas/insertar2.html', context)


def insertarproductora(request):
    if request.method == 'POST':
        form = AgregarProductora(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            nombre = cleaned_data.get('nombre')
            dato = cleaned_data.get('dato')
            productora_model = Productoras.objects.create(nombre=nombre, imagen=dato)
            productora_model.save()
            return render(request, 'peliculas/cerrar.html')
    else:
        form = AgregarProductora()
    context = {'form': form}
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, "peliculas/insertar2.html", context)
