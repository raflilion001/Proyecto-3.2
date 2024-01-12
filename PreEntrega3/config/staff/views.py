from django.shortcuts import render, redirect
from .forms import MiFormulario 

def formulario(request):
    if request.method == "POST":
        formulario = MiFormulario(request.POST)
        if formulario.is_valid():
            # Procesar los datos del formulario aquí
            # Por ejemplo, puedes guardar los datos en la base de datos
            formulario.save()
            return redirect('staff')  # Redirigir a la página de staff después de procesar el formulario
    else:
        formulario = MiFormulario()

    return render(request, "staff/index_formulario.html", {'formulario': formulario})
