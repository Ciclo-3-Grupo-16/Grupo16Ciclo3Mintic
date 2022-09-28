from django.db import models

# Create your models here.

class Empleado(models.Model):
    identificacion = models.IntegerField(primary_key=True) 
    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    departamento = models.CharField(max_length=30)
    municipio = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    celular = models.CharField(max_length=15)
    correo = models.CharField(max_length=20)  
    cargo = models.CharField(max_length=20)


class Usuario(models.Model):
    nombre_usuario = models.CharField(primary_key=True, max_length=10)
    identificacion = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    clave = models.CharField(max_length=10)
    rol = models.CharField(max_length=20)
      
class Empresa(models.Model):
    nit = models.IntegerField(primary_key=True) 
    nombre_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    actividad_economica = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    departamento = models.CharField(max_length=30)
    municipio = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=40)
    
    #def __str__(self) -> str:
    #    return '%s %s %s %s %s %s %s %s %s %s' %(self.nit, self.nombre_usuario, self.nombre, self.actividad_economica,
    #    self.pais, self.departamento, self.municipio, self.direccion, self.telefono, self.correo)

class Ingresos_Gastos(models.Model):
    nombre_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nit = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    ingresos = models.FloatField()
    gastos = models.FloatField()

    def __str__(self) -> str:
        return '%s %s %s %s' %(self.nombre_usuario, self.nit, self.ingresos, self.gastos) #Para mostrar los datos, notación django
    