from django.shortcuts import render, redirect
from .forms import SugerenciaForm

def formulario_sugerencia(request):
    if request.method == "POST":
        formulario = SugerenciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sugerencias:index')  # Ajusta la URL según tu configuración
    else:
        formulario = SugerenciaForm()

    return render(request, "sugerencias/index_sugerencia.html", {'formulario': formulario})
