from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'prioridad', 'fecha_limite']
        widgets = {
            'fecha_limite': forms.DateTimeInput(attrs={'type':'datetime-local'}),
        }