from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from core.models import Person, Nacionality
from django.db.models import Q


def index(request):

    if request.method == 'POST':
        name = request.POST['name']
        last_name = request.POST['last_name']
        birthday = request.POST['birthday']
        name = request.POST['name']
        nacionality_id = request.POST['nacionality_id']
        age = request.POST['age']
        descripcion = request.POST['descripcion']

        try:
            nacionality = Nacionality.objects.get(id = nacionality_id)
            Person.objects.create(
                name = name,
                last_name= last_name,
                birthday = birthday,
                nacionality = nacionality,
                age = age,
                descripcion = descripcion
            )
            print('Datos creados corretamente')
        except Exception as e:
            print('Hubo un error al guardar los datos: ', e)
        
        return redirect('home')

    persons = Person.objects.all()
    nacionalities = Nacionality.objects.all()


    # Optimizar la eliminación de nacionalidades repetidas sin perder Person

    # Obtener la nacionalidad única
    unicamexicana = Nacionality.objects.filter(name__contains='Mexicana').first()

    if unicamexicana:
        # Actualizar todas las personas con nacionalidad Mexicana a la nacionalidad única
        Person.objects.filter(nacionality__id=1).exclude(nacionality=unicamexicana).update(nacionality=unicamexicana)

        # Eliminar los registros de nacionalidades repetidas
        Nacionality.objects.filter(name__contains='Mexicana').exclude(id=unicamexicana.id).delete()

    context = {
        'persons': persons,
        'nacionalities': nacionalities
    }

    return render(request, 'index.html', context)

def cocina(request):
    return render(request, 'cocina.html')