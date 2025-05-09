from django.db import models

<<<<<<< HEAD
# Create your models here.


#Aqui va la logica para la db
=======
class Nacionality(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

category_choices = (
    ('1', 'Estudiante'),
    ('2', 'Trabajador'),
    ('3', 'Desempleado'),
)

class Person(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    last_name = models.CharField(max_length=200, verbose_name='Apellido')
    birthday = models.DateField(verbose_name='Fecha de nacimiento')
    nacionality = models.ForeignKey(Nacionality, on_delete=models.CASCADE, related_name='nacionality')
    age = models.PositiveSmallIntegerField(default=0)
    descripcion = models.TextField()
    category = models.CharField(max_length=1, choices=category_choices, default='1')

    def __str__(self):
        return '{} - {}: {}'.format(
            self.name, self.nacionality.name, self.nacionality.id
            )  

>>>>>>> 84d564c90776a49808415d9423991ec8769a41b4
