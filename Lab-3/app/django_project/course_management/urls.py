from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('asignaturas/', views.asignaturas_list, name='asignaturas_list'),
    path('asignaturas/<int:pk>/', views.asignatura_detail, name='asignatura_detail'),
    path('alumnos/', views.alumnos_list, name='alumnos_list'),
    path('alumnos/<int:pk>/', views.alumno_detail, name='alumno_detail'),
    path('agregar_alumno/', views.agregar_alumno, name='agregar_alumno'),
    path('agregar_asignatura/', views.agregar_asignatura, name='agregar_asignatura'),
        path('alumnos/<int:pk>/editar/', views.editar_alumno, name='editar_alumno'),
    path('alumnos/<int:pk>/eliminar/', views.eliminar_alumno, name='eliminar_alumno'),
]