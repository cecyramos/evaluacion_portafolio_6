from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Receta
from .forms import ContactoForm, RegistroForm, LoginForm, RecetaForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

# Página de inicio: muestra las últimas recetas
def inicio(request):
    recetas = Receta.objects.order_by('-id')[:6]  # últimas 6 recetas
    return render(request, 'inicio.html', {'recetas': recetas})

# Página de recetas: lista todas las recetas
class ListaRecetas(ListView):
    model = Receta
    template_name = 'lista_recetas.html'
    context_object_name = 'recetas'

# Página de detalle de receta
def detalle_receta(request, receta_id):
    receta = Receta.objects.filter(id=receta_id).first()
    return render(request, 'detalle_receta.html', {'receta': receta})

# Página de contacto
def contacto(request):
    mensaje = ''
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            return redirect('confirmacion_contacto')
        else:
            mensaje = 'Por favor completa todos los campos correctamente.'
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form, 'mensaje': mensaje})

def confirmacion_contacto(request):
    return render(request, 'confirmacion_contacto.html')

# Registro de usuarios
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('inicio')

# Vista protegida: solo usuarios autenticados pueden crear recetas
@login_required(login_url='login')
def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.autor = request.user
            receta.save()
            return redirect('lista_recetas')
    else:
        form = RecetaForm()
    return render(request, 'crear_receta.html', {'form': form})