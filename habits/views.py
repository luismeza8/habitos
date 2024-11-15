from django.shortcuts import redirect, render

from habits.forms import HabitoForm
from habits.models import Habito


def home(request):
    formulario_habito = HabitoForm()
    habitos = request.user.habito_set.all()
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
    pass
