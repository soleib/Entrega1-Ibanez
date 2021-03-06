from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Locales(models.Model):
    nombrelocal = models.CharField('nombrelocal',max_length=45)
    ciudad = models.CharField('ciudad',max_length=45)
    provincia = models.CharField('provincia',max_length=45)
    direccion = models.CharField('direccion',max_length=45)
    altura = models.IntegerField()
    fechaapertura = models.DateField('fechaapertura')

    def __str__(self):
        return f'{self.nombrelocal} - Ubicación: {self.direccion} {self.altura} - {self.ciudad} {self.provincia}'

class Hamburguesas(models.Model):
    nombrehamburguesa = models.CharField('nombrehamburguesa',max_length=45)
    tipopan = models.CharField('tipopan',max_length=45)
    tipocarne = models.CharField('tipocarne',max_length=45)
    cantidadmedallones = models.IntegerField()
    aderezo = models.CharField('aderezo',max_length=45)
    salsaMrBlack = models.CharField('salsaMrBlack',max_length=45)
    fechacreacion = models.DateField('fechacreacion')
    imagen_referencial=models.ImageField('imagen_referencial',upload_to='imagenes/', max_length=255 , null=True)

    def __str__(self):
        return f'{self.nombrehamburguesa}'


class Contacto(models.Model):
    nombre=models.CharField('Nombre',max_length=100)
    apellidos=models.CharField('Apellidos',max_length=150)
    correo=models.EmailField('Correo Electrónico',max_length=200)
    asunto=models.CharField('Asunto',max_length=200)
    mensaje=models.TextField('Mensaje')
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.asunto


# class Panchos(models.Model):
#     nombrepancho = models.CharField('nombrepancho',max_length=45)
#     tamaño = models.CharField('tipopan',max_length=45)
#     aderezo = models.CharField('aderezo',max_length=45)
#     salsa = models.CharField('salsa',max_length=45)
#     fechacreacion = models.DateField('fechacreacion')

#     def __str__(self):
#         return f'{self.nombrepancho}'

class Avatar(models.Model):
    #vinvulo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Subcaperta avatares de media :) 
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"

