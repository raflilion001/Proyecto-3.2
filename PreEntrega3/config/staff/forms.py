from django import forms

from . import models


class StaffForm(forms.ModelForm):
    class Meta:
        model = models.staff
        fields = "__all__"