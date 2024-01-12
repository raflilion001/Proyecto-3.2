from django.db import models

class Sugerencia(models.Model):
    contenido = models.TextField()
    # Otros campos según tus necesidades

    def __str__(self):
        return f"Sugerencia: {self.contenido[:50]}..."
