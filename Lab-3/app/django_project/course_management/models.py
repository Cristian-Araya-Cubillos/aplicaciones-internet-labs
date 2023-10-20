from django.db import models

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True,default="")

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100, default="")
    apellido_materno = models.CharField(max_length=100,default="")
    fecha_nacimiento = models.DateField(null=True)
    asignaturas = models.ManyToManyField(Asignatura)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
