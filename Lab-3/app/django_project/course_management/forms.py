from django import forms
from .models import Alumno, Asignatura

class AlumnoForm(forms.ModelForm):
    asignaturas = forms.ModelMultipleChoiceField(
        queryset=Asignatura.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Alumno
        fields = '__all__'

class AsignaturaForm(forms.ModelForm):
    alumnos = forms.ModelMultipleChoiceField(
        queryset=Alumno.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Opcional, dependiendo de tus requerimientos
    )

    class Meta:
        model = Asignatura
        fields = ['nombre', 'codigo', 'alumnos']

class AlumnoDeleteForm(forms.Form):
    alumno_a_eliminar = forms.ModelChoiceField(
        queryset=Alumno.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None,
    )