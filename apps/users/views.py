from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroForm, LoginForm


def landing(request):
    """Página de inicio / landing page."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'users/landing.html')


def auth_choice(request):
    """Pantalla de elección: Login o Registro."""
    return render(request, 'users/auth_choice.html')


def registro(request):
    """Registro de nuevo usuario."""
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = RegistroForm()

    return render(request, 'users/registro.html', {'form': form})


def login_view(request):
    """Inicio de sesión."""
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Email o contraseña incorrectos.')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    """Cerrar sesión."""
    logout(request)
    return redirect('landing')


@login_required
def dashboard(request):
    """Dashboard principal del usuario."""
    from apps.routines.models import Rutina
    rutinas = Rutina.objects.filter(usuario=request.user).order_by('-creada_en')[:5]
    return render(request, 'users/dashboard.html', {'rutinas': rutinas})
