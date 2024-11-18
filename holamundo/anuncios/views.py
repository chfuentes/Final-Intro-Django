from . import forms

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib import messages
from .models import Anuncio, TipoAnuncio
from .forms import CrearAnuncio


class ListaAnunciosView(ListView):
    model = Anuncio
    template_name = 'anuncios/lista_anuncios.html'
    context_object_name = 'anuncios'


"""
def lista_anuncios(request):
    anuncios = Anuncio.objects.all()
    return render(request, 'anuncios/lista_anuncios.html', {'anuncios': anuncios})
"""


def otra_lista_anuncios(request):
    anuncios = Anuncio.objects.all()
    return render(request, 'anuncios/otra_lista_anuncios.html', {'anuncios': anuncios})


class CargaPaginaAnuncioView(DetailView):
    model = Anuncio
    template_name = 'anuncios/anuncio.html'
    context_object_name = 'anuncio'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


"""
def pagina_anuncio(request, slug):
    anuncio = Anuncio.objects.get(slug=slug)
    return render(request, 'anuncios/anuncio.html', {'anuncio': anuncio})
"""


class NuevoAnuncioView(CreateView):
    model = Anuncio
    form_class = CrearAnuncio
    template_name = 'anuncios/nuevo_anuncio.html'
    success_url = reverse_lazy('anuncios:listar')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


"""
def nuevo_anuncio(request):
    if request.method == "POST":
        form = forms.CrearAnuncio(request.POST, request.FILES)
        if form.is_valid():
            nuevo_anuncio = form.save(commit=False)
            nuevo_anuncio.autor = request.user
            nuevo_anuncio.save()
            return redirect('anuncios:listar')
    else:
        form = forms.CrearAnuncio()
    return render(request, 'anuncios/nuevo_anuncio.html', {"form": form})
"""


class EditarAnuncioView(UpdateView):
    model = Anuncio
    fields = ['titulo', 'cuerpo', 'tipo', 'imagen']
    template_name = 'anuncios/editar_anuncio_custom.html'
    success_url = reverse_lazy('anuncios:listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipos'] = TipoAnuncio.objects.all()
        return context

    def form_valid(self, form):
        tipo = get_object_or_404(TipoAnuncio, id=self.request.POST['tipo'])
        form.instance.tipo = tipo
        return super().form_valid(form)


"""
def editar_anuncio(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)

    if request.method == 'POST':
        form = forms.CrearAnuncio(
            request.POST, files=request.FILES, instance=anuncio)

        if form.is_valid():
            form.save()
            messages.success(request, "Anuncio modificado correctamente")
            return redirect('anuncios:listar')
    else:
        form = forms.CrearAnuncio(instance=anuncio)

    return render(request, 'anuncios/editar_anuncio.html', {'form': form, 'anuncio': anuncio})
"""


def editar_anuncio_custom(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)
    if request.method == 'POST':
        anuncio.titulo = request.POST['titulo']
        anuncio.cuerpo = request.POST['cuerpo']
        tipo = get_object_or_404(TipoAnuncio, id=request.POST['tipo'])
        anuncio.tipo = tipo
        try:
            if request.FILES['imagen']:
                anuncio.imagen = request.FILES['imagen']
        except:
            pass
        anuncio.save()
        messages.success(request, "Anuncio modificado correctamente")
        return redirect('anuncios:otrolistar')
    else:
        tipos = TipoAnuncio.objects.all()
    return render(request, 'anuncios/editar_anuncio_custom.html', {'anuncio': anuncio, 'tipos': tipos})


class EliminarAnuncioView(DeleteView):
    model = Anuncio
    template_name = 'anuncios/confirmar_eliminar.html'
    success_url = reverse_lazy('anuncios:listar')

    def delete(self, request, *args, **kwargs):
        anuncio = self.get_object()
        messages.success(
            request, f"Anuncio '{anuncio.titulo}' eliminado correctamente")
        return super().delete(request, *args, **kwargs)


"""
def eliminar_anuncio(request, id):
    if request.method == "POST":
        anuncio = get_object_or_404(Anuncio, id=id)
        anuncio.delete()
        messages.success(request, f"Anuncio eliminado correctamente")
        return redirect('anuncios:otrolistar')
    else:
        return redirect('anuncios:otrolistar')
"""
