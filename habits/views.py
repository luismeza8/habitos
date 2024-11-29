from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from datetime import date, datetime, timedelta
from habits.forms import HabitoForm
from habits.models import Habito
from habits.models import Dia
import json

def generar_dias(habito):
    # Define el rango de fechas (del 10/11 al 16/11)
    inicio = date(2024, 11, 10)
    fin = date(2024, 11, 28)

    # Crea un día por cada fecha dentro del rango
    for i in range((fin - inicio).days + 1):
        fecha = inicio + timedelta(days=i)
        Dia.objects.get_or_create(habito=habito, fecha=fecha)

def home(request):
    formulario_habito = HabitoForm()
    habitos = request.user.habito_set.all()
    fechas = []

    for i in range(1, 8):
        dia = (datetime.today() - timedelta(days=i)).strftime('%d/%m')
        fechas.append(dia)

    for habito in habitos:
        generar_dias(habito)


    return render(request, 'habits/home.html', {'form': formulario_habito, 'habitos': habitos, 'fechas': fechas})

def crear_habito(request):
    if request.method == 'POST':
        formulario_habito = HabitoForm(request.POST)

        if formulario_habito.is_valid():
            habito = formulario_habito.save(commit=False)
            habito.usuario = request.user
            habito.save()
            return redirect('home')

    return render(request, 'habits/home.html')

def borrar_habito(_, pk):
    habito = Habito.objects.get(pk=pk)
    habito.delete()
    return redirect('home')

def editar_habito(request, pk):
    habito = Habito.objects.get(pk=pk)

    if request.method == 'POST':
        formulario_habito = HabitoForm(request.POST, instance=habito)

        if formulario_habito.is_valid():
            formulario_habito.save()
            return redirect('home')

    else:
        formulario_habito = HabitoForm(instance=habito)

    return render(request, 'habits/editar_habito.html', {'form': formulario_habito, 'habito': habito})

def alternar_dia(_, pk):
    dia = get_object_or_404(Dia, pk=pk)
    dia.realizado = not dia.realizado  # Alterna el estado de "realizado"
    dia.save()
    
    return redirect('home') 

def grafica_habito(request, habit_id):
    habit = get_object_or_404(Habito, id=habit_id)
    
    actividades = habit.obtener_ultimos_7_dias()

    realizado_count = sum(1 for actividad in actividades if actividad.realizado)
    no_realizado_count = len(actividades) - realizado_count

    realizado_json = json.dumps(realizado_count)
    no_realizado_json = json.dumps(no_realizado_count)

    return render(request, 'habits/grafica_habito.html', {
        'habit_id': habit_id,
        'realizado_json': realizado_json,
        'no_realizado_json': no_realizado_json,
    })