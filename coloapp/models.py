from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Tarea(models.Model):
    PRIORIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('urgente', '¡Para ayer!'),
    ]

    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='media')
    fecha_inicio = models.DateTimeField(default=timezone.now)
    fecha_limite = models.DateTimeField()
    completada = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.get_prioridad_display()})"