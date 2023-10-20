from django.contrib import admin
from .models import Alumno
from .models import Asignatura

admin.site.register(Alumno)
admin.site.register(Asignatura)