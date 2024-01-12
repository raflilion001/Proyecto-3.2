from django import forms

from . import models


class StaffForm(forms.ModelForm):
    class Meta:
        model = models.staff
        fields = "__all__"   #indica que se deben incluir todos los campos del modelo en el formulario.
        #Es un atajo que le dice a Django que incluya todos los campos del modelo en el formulario.