from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CaloriasForm, IMCForm
from .models import CalculoCaloria


@login_required
def herramientas(request):
    return render(request, 'tools/herramientas.html')


@login_required
def calculadora_calorias(request):
    resultado = None
    form = CaloriasForm()

    if request.method == 'POST':
        form = CaloriasForm(request.POST)
        if form.is_valid():
            calculo = form.save(commit=False)
            calculo.usuario = request.user
            calculo.calcular()
            calculo.save()
            resultado = calculo

    return render(request, 'tools/calculadora_calorias.html', {
        'form': form,
        'resultado': resultado,
    })


@login_required
def calculadora_imc(request):
    resultado = None
    form = IMCForm()

    if request.method == 'POST':
        form = IMCForm(request.POST)
        if form.is_valid():
            altura_m = form.cleaned_data['altura'] / 100
            peso = form.cleaned_data['peso']
            imc = round(peso / (altura_m ** 2), 1)

            # Categoría
            if imc < 16:
                categoria = "Delgadez Severa"
                riesgo = "Muy Alto"
                color = "danger"
                cambiar = "Subir peso"
            elif imc < 17:
                categoria = "Delgadez Moderada"
                riesgo = "Alto"
                color = "danger"
                cambiar = "Subir peso"
            elif imc < 18.5:
                categoria = "Delgadez Leve"
                riesgo = "Moderado"
                color = "warning"
                cambiar = "Subir peso"
            elif imc < 25:
                categoria = "Peso Normal"
                riesgo = "Normal"
                color = "success"
                cambiar = "No"
            elif imc < 30:
                categoria = "Sobre peso"
                riesgo = "Aumentado"
                color = "warning"
                cambiar = "Bajar peso"
            elif imc < 35:
                categoria = "Obesidad Clase 1"
                riesgo = "Alto"
                color = "orange"
                cambiar = "Bajar peso"
            elif imc < 40:
                categoria = "Obesidad Clase 2"
                riesgo = "Muy Alto"
                color = "danger"
                cambiar = "Bajar peso"
            else:
                categoria = "Obesidad Clase 3"
                riesgo = "Extremo"
                color = "danger"
                cambiar = "Bajar peso urgente"

            altura_cm = form.cleaned_data['altura']
            peso_min = round(18.5 * (altura_m ** 2), 1)
            peso_max = round(24.9 * (altura_m ** 2), 1)

            resultado = {
                'imc': imc,
                'categoria': categoria,
                'riesgo': riesgo,
                'color': color,
                'cambiar': cambiar,
                'peso_min': peso_min,
                'peso_max': peso_max,
                'altura': altura_cm,
                'peso': peso,
            }

    return render(request, 'tools/calculadora_imc.html', {
        'form': form,
        'resultado': resultado,
    })
