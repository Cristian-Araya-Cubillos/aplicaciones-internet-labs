from django.shortcuts import render, redirect, get_object_or_404
from .models import Asignatura, Alumno
from .forms import AlumnoForm, AsignaturaForm, AlumnoDeleteForm

def index(request):
    # Obtén la lista de asignaturas
    asignaturas = Asignatura.objects.all()

    # Calcula la cantidad de alumnos para cada asignatura
    asignaturas_con_alumnos = []
    for asignatura in asignaturas:
        cantidad_alumnos = Alumno.objects.filter(asignaturas=asignatura).count()
        asignaturas_con_alumnos.append({
            'asignatura': asignatura,
            'cantidad_alumnos': cantidad_alumnos,
        })

    # Configura las migas de pan
    breadcrumbs = [{'text': 'Home', 'url': '/'}]

    # Renderiza la plantilla y pasa los datos al contexto
    return render(request, 'index.html', {'asignaturas_con_alumnos': asignaturas_con_alumnos, 'breadcrumbs': breadcrumbs})

def asignaturas_list(request):
    breadcrumbs = [{'text': 'Home', 'url': '/'}, {'text': 'Asignaturas', 'url': '/asignaturas/'}]
    asignaturas = Asignatura.objects.all()
    return render(request, 'asignaturas_list.html', {'asignaturas': asignaturas, 'breadcrumbs': breadcrumbs})

def asignatura_detail(request, pk):
    breadcrumbs = [{'text': 'Home', 'url': '/'}, {'text': 'Asignaturas', 'url': '/asignaturas/'}, {'text': 'Detalle de Asignatura', 'url': '/asignaturas/{}/'.format(pk)}]
    asignatura = get_object_or_404(Asignatura, pk=pk)
    return render(request, 'asignatura_detail.html', {'asignatura': asignatura, 'breadcrumbs': breadcrumbs})

def alumnos_list(request):
    breadcrumbs = [{'text': 'Home', 'url': '/'}, {'text': 'Alumnos', 'url': '/alumnos/'}]
    alumnos = Alumno.objects.all()
    form = AlumnoDeleteForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        alumno_a_eliminar = form.cleaned_data['alumno_a_eliminar']
        alumno = get_object_or_404(Alumno, pk=alumno_a_eliminar.pk)
        alumno.delete()
        return redirect('alumnos_list')

    return render(request, 'alumnos_list.html', {'alumnos': alumnos, 'form': form, 'breadcrumbs': breadcrumbs})

def alumno_detail(request, pk):
    breadcrumbs = [{'text': 'Home', 'url': '/'}, {'text': 'Alumnos', 'url': '/alumnos/'}, {'text': 'Detalle de Alumno', 'url': '/alumnos/{}/'.format(pk)}]
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'alumno_detail.html', {'alumno': alumno, 'breadcrumbs': breadcrumbs})


def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumnos_list')  # Redirigir a la página de lista de alumnos
    else:
        form = AlumnoForm()
    
    breadcrumbs = [{'text': 'Home', 'url': '/'}, {'text': 'Alumnos', 'url': '/alumnos/'}, {'text': 'Agregar Alumno', 'url': '/agregar_alumno/'}]
    return render(request, 'agregar_alumno.html', {'form': form, 'breadcrumbs': breadcrumbs})


def agregar_asignatura(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asignaturas_list')  # Redirige a la lista de asignaturas
    else:
        form = AsignaturaForm()
    breadcrumbs = [{'text': 'Home', 'url': '/'}, {'text': 'Asignaturas', 'url': '/asignaturas/'}, {'text': 'Agregar Asignatura', 'url': '/agregar_asignatura/'}]
    return render(request, 'agregar_asignatura.html', {'form': form, 'breadcrumbs': breadcrumbs})

#Eliminar/Editar Alumnos
def editar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('alumnos_list')
    else:
        form = AlumnoForm(instance=alumno)
    
    return render(request, 'editar_alumno.html', {'form': form, 'alumno': alumno})

def eliminar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    
    if request.method == 'POST':
        alumno.delete()
        return redirect('alumnos_list')
    
    return render(request, 'eliminar_alumno.html', {'alumno': alumno})