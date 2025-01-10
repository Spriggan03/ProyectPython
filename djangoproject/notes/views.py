from django.shortcuts import render, redirect, get_object_or_404
from .models import Nota
from .forms import NotaForm

def lista_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notes/lista_notas.html', {'notas': notas})

def crear_nota(request):
    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm()
    return render(request, 'notes/crear_nota.html', {'form': form})

def editar_nota(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == "POST":
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm(instance=nota)
    return render(request, 'notes/editar_nota.html', {'nota': nota})

def eliminar_nota(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == "POST":
        nota.delete()
        return redirect('lista_notas')
    return render(request, 'notes/eliminar_nota.html', {'nota': nota})

