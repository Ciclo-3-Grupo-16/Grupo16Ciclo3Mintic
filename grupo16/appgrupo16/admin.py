from django.contrib import admin

# Register your models here.

from appgrupo16.models import Empleado, Usuario, Empresa, Ingresos_Gastos 

admin.site.register(Empleado)
admin.site.register(Usuario)
admin.site.register(Empresa)
admin.site.register(Ingresos_Gastos)