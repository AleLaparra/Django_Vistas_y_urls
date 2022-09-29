from django.db import models

# Create your models here.
class Estudiante (models.Model):
    nombre= models.CharField (max_length =100)
    apellido = models.CharField (max_length = 200)
    creacion= models.DateTimeField (auto_now_add =True)


    def _str_(self):
        return '%s %s' % (self.nombre, self.apellido)


class Curso (models.Model):
    nombre = models.CharField (max_length = 100)
    creacion= models.DateTimeField (auto_now_add =True)
    Estudiante = models.ManyToManyField(Estudiante)

    def _str_(self):
        return '%s %s' % (self.nombre)

    
class Telefono (models.Model):
    tipo_telefono = (

        ('C', 'Casa'),
        ('M', 'Celular'),
        ('T', 'Trabajo'),
    )
    telefono= models.CharField (max_length =13)
    estudiante= models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    tipo = models.CharField (
        max_length=1,
        choices=tipo_telefono,
        default='C',
    )
    creacion= models.DateTimeField (auto_now_add =True)


    def _str_(self):
       return '%s ' % (self.telefono)
