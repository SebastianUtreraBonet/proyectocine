import datetime
from .models import *
from django import forms


class AgregarActor(forms.Form):
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))

    fecha = forms.DateField(label="Fecha de nacimiento",
                            widget=forms.DateInput(attrs={'class': 'form-control'}))
    imagen = forms.ImageField(label="Foto")
    pais = forms.ModelChoiceField(queryset=Paises.objects.all().order_by('nombre'), label="Pais",
                                  widget=forms.Select(attrs={'class': 'form-control'}))

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if Paises.objects.filter(nombre=nombre):
            raise forms.ValidationError('Ya existe un ACTOR con ese nombre en la db.')
        return nombre

    def clean_foto(self):
        imagen = self.cleaned_data['bandera']
        if Paises.objects.filter(foto=imagen):
            raise forms.ValidationError('Ya existe una foto igual en la db.')
        return imagen


class AgregarDirector(forms.Form):
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    pais = forms.ModelChoiceField(queryset=Paises.objects.all().order_by('nombre'), label="Paises",
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    fecha = forms.DateField(label="Fecha de nacimiento",
                            widget=forms.DateInput(attrs={'class': 'form-control'}))
    imagen = forms.ImageField(label="Foto")

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if Paises.objects.filter(nombre=nombre):
            raise forms.ValidationError('Ya existe un pais con ese nombre en la db.')
        return nombre

    def clean_foto(self):
        imagen = self.cleaned_data['imagen']
        if Paises.objects.filter(foto=imagen):
            raise forms.ValidationError('Ya existe una foto igual en la db.')
        return imagen


class AgregarGenero(forms.Form):
    genero = forms.CharField(label="Genero", widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_genero(self):
        """Comprueba que no exista un username igual en la db"""
        genero = self.cleaned_data['genero']
        if Paises.objects.filter(nombre=genero):
            raise forms.ValidationError('Ya existe un pais con ese nombre en la db.')
        return genero


class AgregarPelicula(forms.Form):
    a = timezone.datetime.now()
    titulo = forms.CharField(label="Titulo", widget=forms.TextInput(attrs={'class': 'form-control'}))
    actores = forms.ModelMultipleChoiceField(queryset=Actores.objects.all().order_by('nombre'), label="Actores",
                                             widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    director = forms.ModelChoiceField(queryset=Directores.objects.all().order_by('nombre'), label="Director",
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    anio = forms.IntegerField(label="Año", widget=forms.NumberInput(attrs={'class': 'form-control'}), max_value=a.year,
                              min_value=1920, initial=a.year)
    sinopsis = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label="Sipnosis")
    genero = forms.ModelMultipleChoiceField(queryset=Generos.objects.all().order_by('genero'), label="Genero",
                                            widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    pais = forms.ModelChoiceField(queryset=Paises.objects.all().order_by('nombre'),
                                  widget=forms.Select(attrs={'class': 'form-control'}), label="Pais")
    productora = forms.ModelChoiceField(queryset=Productoras.objects.all().order_by('nombre'),
                                        widget=forms.Select(attrs={'class': 'form-control'}), label="Productora")
    caratula = forms.ImageField(required=False, label="Caratula")

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if Peliculas.objects.filter(titulo=titulo):
            raise forms.ValidationError('Ya existe un usuario con ese nombre en la db.')
        return titulo

    def clean_caratula(self):
        caratula = self.cleaned_data['caratula']
        if Peliculas.objects.filter(caratula=caratula):
            raise forms.ValidationError('Ya existe un email igual en la db.')
        return caratula


class AgregarProductora(forms.Form):
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    dato = forms.ImageField(label="Imagen")

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if Paises.objects.filter(nombre=nombre):
            raise forms.ValidationError('Ya existe una productora con ese nombre en la db.')
        return nombre

    def clean_imagen(self):
        dato = self.cleaned_data['dato']
        if Paises.objects.filter(imagen=dato):
            raise forms.ValidationError('Ya existe una imagen igual en la db.')
        return dato


class AgregarPais(forms.Form):
    nombre = forms.CharField(label="Pais", widget=forms.TextInput(attrs={'class': 'form-control'}))
    bandera = forms.ImageField(label="Bandera")

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if Paises.objects.filter(nombre=nombre):
            raise forms.ValidationError('Ya existe un pais con ese nombre en la db.')
        return nombre

    def clean_bandera(self):
        bandera = self.cleaned_data['bandera']
        if Paises.objects.filter(bandera=bandera):
            raise forms.ValidationError('Ya existe una bandera igual en la db.')
        return bandera
