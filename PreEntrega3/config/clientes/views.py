from django.shortcuts import render, redirect
from .forms import ClienteForm

def formulario_cliente(request):
    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('clientes:index')  # Ajusta la URL según tu configuración
    else:
        formulario = ClienteForm()

    return render(request, "clientes/index_cliente.html", {'formulario': formulario})
