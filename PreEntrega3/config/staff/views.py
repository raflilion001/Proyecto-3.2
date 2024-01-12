from django.shortcuts import render, redirect
from .forms import StaffForm

def formulario(request):
    if request.method == "POST":
        formulario = StaffForm(request.POST)
        if formulario.is_valid():
            # Procesar los datos del formulario
            #  guarda los datos en la base de datos
            formulario.save()
            return redirect('staff')  # Redirigir a la página de staff después de procesar el formulario
    else:
        formulario = StaffForm()

    return render(request, "staff/index_formulario.html", {'formulario': formulario})
