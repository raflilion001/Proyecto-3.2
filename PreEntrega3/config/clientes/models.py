from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    # Otros campos según tus necesidades

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"