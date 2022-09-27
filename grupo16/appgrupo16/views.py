from email import message
import json
from re import template
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from .models import Empleado
from .models import Empresa
from .models import Ingresos_Gastos
from .models import Usuario

from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class EmpleadoViews(View): 
    @method_decorator(csrf_exempt) #Método para evitar problema de seguridad
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self, request, id=0):   #Método buscar un dato y después del último else es el metodo de ver datos

        if id>0:
            emple=list(Empleado.objects.filter(identificacion=id).values())
            if len (emple)>0:
                emplrespuesta=emple[0]
                datos={"empleado": emplrespuesta}
            else:
                datos={"Respuesta":"El Dato No Existe"}

        else:
            template_name="consultarempleado.html"
            emple=Empleado.objects.all()
            datos={'empleado': emple}
        
        return render(request, template_name, datos)
  

    def post(self, request):
        template_name="agregarempleado.html"
        #datos=json.loads(request.body)
        Empleado.objects.create(identificacion=request.POST["identificacion"],nombre=request.POST["nombre"], 
        apellido=request.POST["apellido"], pais=request.POST["pais"], departamento=request.POST["departamento"],
        municipio=request.POST["municipio"], direccion=request.POST["direccion"], celular=request.POST['celular'],
        correo=request.POST["correo"], cargo=request.POST["cargo"])
        return redirect('/gestionadmin/')

    #método actualizar
    def put(self,request,id):
        datos=json.loads(request.body)
        #consultar datos
        empl=list(Empleado.objects.filter(identificacion=id).values())
        
        if len(empl)>0:
            empleados=Empleado.objects.get(identificacion=id)
            empleados.nombre=datos['nombre']
            empleados.apellido=datos['apellido']
            empleados.pais=datos['pais']
            empleados.departamento=datos['departamento']
            empleados.municipio=datos['municipio']
            empleados.direccion=datos['direccion']
            empleados.celular=datos['celular']
            empleados.correo=datos['correo']
            empleados.cargo=datos['cargo']
            empleados.save()
            mensaje={'Respuesta':"Datos Actualizados"}
        
        else:
            mensaje={'Respuesta':"El Dato No existe"}
        
        return JsonResponse(mensaje)

#Método eliminar
    def delete(self,request,id):
        empl=list(Empleado.objects.filter(identificacion=id).values())
       
        if len(empl)>0:
            Empleado.objects.filter(identificacion=id).delete()
            mensaje={"Respuesta":"Datos Eliminados"}
        
        else:
            mensaje={'Respuesta':"El Dato No existe"}

        return JsonResponse(mensaje)

class UsuarioViews(View): 
    @method_decorator(csrf_exempt) #Método para evitar problema de seguridad
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self, request, nous=""):   #Método buscar un dato y después del último else es el metodo de ver datos

        if nous!="":
            usu=list(Usuario.objects.filter(nombre_usuario=nous).values())
            if len (usu)>=0:
                usurespuesta=usu[0]
                datos={"usuario": usurespuesta}
            else:
                datos={"Respuesta":"El Dato No Existe"}

        else:
            template_name="consultarusuario.html"
            usu=Usuario.objects.all()
            datos={'usuario': usu}
        
        return render(request, template_name, datos)

    def post(self, request):
        template_name="agregarusuario.html"
        #datos=json.loads(request.body)
        #try:
        emp=Empleado.objects.get(identificacion=request.POST["identificacion"])
        usu= Usuario.objects.create(nombre_usuario=request.POST["nombre_usuario"], rol=request.POST['rol'], clave=request.POST["clave"],
        identificacion=emp)
        usu.save()
        #mensaje={"mensaje":"Guardado"}
        return redirect('/gestionadmin/')
        #except Usuario.DoesNotExist:
         #   mensaje={"mensaje":"No Guardado"}
        #return JsonResponse(mensaje)

    def put(self,request,nous):
        datos=json.loads(request.body)
        
        usu=list(Usuario.objects.filter(nombre_usuario=nous).values())
        
        if len(usu)>0:
            usuarios=Usuario.objects.get(nombre_usuario=nous)
            usuarios.clave=datos['clave']
            usuarios.rol=datos['rol']
            usuarios.save()
            mensaje={'Respuesta':"Datos Actualizados"}
        
        else:
            mensaje={'Respuesta':"El Dato No existe"}
        
        return JsonResponse(mensaje)

    def delete(self,request,nous):
        usu=list(Usuario.objects.filter(nombre_usuario=nous).values())
       
        if len(usu)>0:
            Usuario.objects.filter(nombre_usuario=nous).delete()
            mensaje={"Respuesta":"Datos Eliminados"}
        
        else:
            mensaje={'Respuesta':"El Dato No existe"}

        return JsonResponse(mensaje)
    
#Función para el Login
def loginusuario(request):
    if request.method=='POST':
        try:
            #capturar datos desde el formulario
            detalleusuario=Usuario.objects.get(nombre_usuario=request.POST['nomusuario'], clave=request.POST['clave']) #Se captura el del login
            if detalleusuario.rol=='administrador':
                request.session['nomusuario']=detalleusuario.nombre_usuario
                return render(request,'gestionadmin.html')
            elif detalleusuario.rol=="empleado":
                request.session['nomusuario']=detalleusuario.nombre_usuario
                return render(request, 'gestionempleado.html')
        except Usuario.DoesNotExist as e:
            message.success(request, "No Existe el Dato")
    return render(request, 'login.html')

class EmpresaViews(View): 
    @method_decorator(csrf_exempt) #Método para evitar problema de seguridad
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self, request, nit=0):   #Método buscar un dato y después del último else es el metodo de ver datos

        if nit>0:
            empr=list(Empresa.objects.filter(nit=nit).values())
            if len (empr)>=0:
                emprrespuesta=empr[0]
                datos={"empresa": emprrespuesta}
            else:
                datos={"Respuesta":"El Dato No Existe"}

        else:
            template_name="consultarempresa.html"
            empr=Empresa.objects.all()
            datos={'empresa': empr}
        
        return render(request, template_name, datos)

    def post(self, request):
        template_name="agregarempresa.html"        
        #try:
        usua=Usuario.objects.get(nombre_usuario=request.POST["nombre_usuario"])
        emp= Empresa.objects.create(nit=request.POST["nit"], nombre=request.POST["nombre"], actividad_economica=request.POST["actividad_economica"], 
        pais=request.POST["pais"], departamento=request.POST["departamento"], municipio=request.POST["municipio"], direccion=request.POST["direccion"], 
        telefono=request.POST["telefono"], correo=request.POST["correo"], nombre_usuario=usua)
        emp.save()
            #mensaje={"mensaje":"Guardado"}
        return redirect('/gestionadmin/')
        #except Usuario.DoesNotExist:
            #mensaje={"mensaje":"No Guardado"}
        #return JsonResponse(mensaje) 

    def put(self,request,nit):
        datos=json.loads(request.body)
        #consultar datos
        empr=list(Empresa.objects.filter(nit=nit).values())
        
        if len(empr)>0:
            empresas=Empresa.objects.get(nit=nit)
            empresas.nombre=datos['nombre']
            empresas.actividad_economica=datos['actividad_economica']
            empresas.pais=datos['pais']
            empresas.departamento=datos['departamento']
            empresas.municipio=datos['municipio']
            empresas.direccion=datos['direccion']
            empresas.telefono=datos['telefono']
            empresas.correo=datos['correo']
            empresas.save()
            mensaje={'Respuesta':"Datos Actualizados"}
        
        else:
            mensaje={'Respuesta':"El Dato No existe"}
        
        return JsonResponse(mensaje)   

    def delete(self,request,nit):
        empr=list(Empresa.objects.filter(nit=nit).values())
       
        if len(empr)>0:
            Empresa.objects.filter(nit=nit).delete()
            mensaje={"Respuesta":"Datos Eliminados"}
        
        else:
            mensaje={'Respuesta':"El Dato No existe"}

        return JsonResponse(mensaje)

class Ingresos_GastosViews(View): 
    @method_decorator(csrf_exempt) #Método para evitar problema de seguridad
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self, request, nit=0):   #Método buscar un dato y después del último else es el metodo de ver datos

        if nit>0:
            ig=list(Ingresos_Gastos.objects.filter(nit=nit).values())
            if len (ig)>=0:
                igrespuesta=ig[0]
                datos={"ingresos_gastos": igrespuesta}
            else:
                datos={"Respuesta":"El Dato No Existe"}

        else:
            template_name="consultarGI.html"
            ig=Ingresos_Gastos.objects.all()
            datos={'ingresos_gastos': ig}

        return render(request, template_name,datos)

    def post(self, request):
        template_name="agregarGI.html"
        #try:
        usu=Usuario.objects.get(nombre_usuario=request.POST["nombre_usuario"])
        emp=Empresa.objects.get(nit=request.POST["nit"])
        ig= Ingresos_Gastos.objects.create(ingresos=request.POST["ingresos"], gastos=request.POST["gastos"],
        nombre_usuario=usu, nit=emp)
        ig.save()
        #mensaje={"mensaje":"Guardado"}
        return redirect('/gestionempleado/')
        #except Usuario.DoesNotExist:
         #   mensaje={"mensaje":"No Guardado"}
        #return JsonResponse(mensaje)

    def delete(self,request,nit):
        ig=list(Ingresos_Gastos.objects.filter(nit=nit).values())
       
        if len(ig)>0:
            Ingresos_Gastos.objects.filter(nit=nit).delete()
            mensaje={"Respuesta":"Datos Eliminados"}
        
        else:
            mensaje={'Respuesta':"El Dato No existe"}

        return JsonResponse(mensaje)

def formularioregistro(request):
    return render(request,"agregarempresa.html")

def gestionadmin(request):
   return render(request,"gestionadmin.html")

def formularioregistroempleado(request):
    return render(request,"agregarempleado.html")

def formularioregistrousuario(request):
    return render(request,"agregarusuario.html")

def formularioregistroingresosgastos(request):
    return render(request,"agregarGI.html")

def gestionempleado(request):
   return render(request,"gestionempleado.html")

def gestionempleado(request):
   return render(request,"gestionempleado.html")

def actualizarempresa(request, nit):
    empresa=Empresa.objects.get(nit=nit)
    datos={
        'empresa':empresa
    }
    print(empresa.nombre)

    return render(request, "actualizarempresa.html", datos)

def actempresa(request):
    n=request.POST['nit']
    nom=request.POST['nombre']
    aec=request.POST['actividad_economica']
    p=request.POST['pais']
    d=request.POST['departamento']
    m=request.POST['municipio']
    d=request.POST['direccion']
    t=request.POST['telefono']
    c=request.POST['correo']
    emp=Empresa.objects.get(nit=n)
    emp.nombre=nom
    emp.actividad_economica=aec
    emp.pais=p
    emp.departamento=d
    emp.municipio=m
    emp.direccion=d
    emp.telefono=t
    emp.correo=c
    emp.save()
    return redirect('/empresa/')

def actualizarempleado(request, identificacion):
    empleado=Empleado.objects.get(identificacion=identificacion)
    datos={
        'empleado':empleado
    }

    return render(request, "actualizarempleado.html", datos)

def actempleado(request):
    identificacion=request.POST['identificacion']
    nom=request.POST['nombre']
    ap=request.POST['apellido']
    p=request.POST['pais']
    d=request.POST['departamento']
    m=request.POST['municipio']
    dir=request.POST['direccion']
    cel=request.POST['celular']
    c=request.POST['correo']
    cg=request.POST['cargo']
    empl=Empleado.objects.get(identificacion=identificacion)
    empl.nombre=nom
    empl.apellido=ap
    empl.pais=p
    empl.departamento=d
    empl.municipio=m
    empl.direccion=dir
    empl.celular=cel
    empl.correo=c
    empl.cargo=cg
    empl.save()
    return redirect('/empleado/')

def actualizarusuario(request, nombre_usuario):
    usuario=Usuario.objects.get(nombre_usuario=nombre_usuario)
    datos={
        'usuario':usuario
    }

    return render(request, "actualizarusuario.html", datos)

def actusuario(request):
    nombre_usuario=request.POST['nombre_usuario']
    c=request.POST['clave']
    r=request.POST['rol']
    usu=Usuario.objects.get(nombre_usuario=nombre_usuario)
    usu.clave=c
    usu.rol=r
    usu.save()
    return redirect('/usuario/')

def eliminarusuario(request, nombre_usuario):
    Usuario.objects.filter(nombre_usuario=nombre_usuario).delete()
    return redirect('/usuario/')

def eliminarempleado(request, identificacion):
    Empleado.objects.filter(identificacion=identificacion).delete()
    return redirect('/empleado/')

def eliminarempresa(request, nit):
    Empresa.objects.filter(nit=nit).delete()
    return redirect('/empresa/')

def consultarjoin(request, nit):
    datos=Ingresos_Gastos.objects.select_related('nit').filter(nit=nit)
    print(datos)
    template_name="consultadatosingresos_gastos.html"
    dat={"lista":datos}
    return render(request,template_name,dat)