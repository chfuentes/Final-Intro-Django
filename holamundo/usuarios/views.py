from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.


@login_required(login_url="/usuarios/login")
@user_passes_test(lambda u: u.is_superuser)
def vista_registro(request):
    if request.method == "POST":
        # Logica del procesamiento del formulario
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente")
            return redirect("anuncios:listar")
    else:
        form = UserCreationForm()
    return render(request, "usuarios/registro.html", {"form": form})


def vista_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request,  f"El usuario {usuario} inició sesión")
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("anuncios:listar")
    else:
        form = AuthenticationForm()
    return render(request, "usuarios/login.html", {"form": form})


def vista_logout(request):
    if request.method == "POST":
        usuario = request.user
        request.session.flush()
        logout(request)
        messages.success(request, f"El usuario {usuario} cerró sesión")
        return redirect("anuncios:listar")

