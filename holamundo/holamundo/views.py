from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class PaginaInicioView(View):
    template_name = 'inicio.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            nombre_usuario = request.user.username
            request.session['nombre_usuario'] = nombre_usuario
            if 'visitas' in request.session:
                request.session['visitas'] += 1
            else:
                request.session['visitas'] = 1
            visitas = request.session['visitas']
            mensaje = f"Bienvenido {nombre_usuario}. Has visitado esta página {visitas} veces."
        else:
            mensaje = "Bienvenido visitante. Por favor, inicia sesión para ver más detalles."

        return render(request, self.template_name, {'mensaje': mensaje})


class PaginaAcercaDeView(TemplateView):
    template_name = 'acerca.html'


class OtraPaginaView(View):
    template_name = 'otra_pagina.html'

    def get(self, request, *args, **kwargs):
        nombre_usuario = request.session.get('nombre_usuario', 'Visitante')
        return render(request, self.template_name, {'nombre_usuario': nombre_usuario})


# Codigo comentado de la vista basada en funciones
""" from django.shortcuts import render


def pagina_inicio(request):
    if request.user.is_authenticated:
        nombre_usuario = request.user.username
        request.session['nombre_usuario'] = nombre_usuario
        if 'visitas' in request.session:
            request.session['visitas'] += 1
        else:
            request.session['visitas'] = 1
        visitas = request.session['visitas']
        mensaje = f"Bienvenido {nombre_usuario}. Has visitado esta página {visitas} veces."
    else:
        mensaje = "Bienvenido visitante. Por favor, inicia sesión para ver más detalles."

    return render(request, 'inicio.html', {'mensaje': mensaje})


def pagina_acerca_de(request):
    return render(request, 'acerca.html')


def otra_pagina(request):
    nombre_usuario = request.session.get('nombre_usuario', 'Visitante')
    return render(request, 'acerca.html', {'nombre_usuario': nombre_usuario}) """
