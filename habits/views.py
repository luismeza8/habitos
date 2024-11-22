from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from datetime import date, timedelta
from habits.forms import HabitoForm
from habits.models import Habito
from habits.models import Dia

def generar_dias(habito):
    # Define el rango de fechas (del 10/11 al 16/11)
    inicio = date(2024, 11, 10)
    fin = date(2024, 11, 16)

    # Crea un día por cada fecha dentro del rango
    for i in range((fin - inicio).days + 1):
        fecha = inicio + timedelta(days=i)
        Dia.objects.get_or_create(habito=habito, fecha=fecha)

def home(request):
    formulario_habito = HabitoForm()
    habitos = request.user.habito_set.all()

    # Genera días automáticamente para cada hábito
    for habito in habitos:
        generar_dias(habito)

    return render(request, 'habits/home.html', {'form': formulario_habito, 'habitos': habitos})

def crear_habito(request):
    if request.method == 'POST':
        formulario_habito = HabitoForm(request.POST)

        if formulario_habito.is_valid():
            habito = formulario_habito.save(commit=False)
            habito.usuario = request.user
            habito.save()
            return redirect('home')

    return render(request, 'habits/home.html')

def borrar_habito(request, pk):
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

def alternar_dia(request, pk):
    dia = get_object_or_404(Dia, pk=pk)
    dia.realizado = not dia.realizado  # Alterna el estado de "realizado"
    dia.save()
    
    return redirect('home') 
        


        