from django.urls import path
from .views import EmpleadoViews
from .views import UsuarioViews
from .views import EmpresaViews
from .views import Ingresos_GastosViews
from .import views

urlpatterns= [
    
    path('empleado/', EmpleadoViews.as_view(), name='Listar'),
    path('empleado/<int:id>', EmpleadoViews.as_view(), name='Actualizar'),
    path('usuario/', UsuarioViews.as_view(), name='Listar'),
    path('usuario/<str:nous>', UsuarioViews.as_view(), name='Actualizar'),
    path('empresa/', EmpresaViews.as_view(), name='Listar'),
    path('empresa/<int:nit>', EmpresaViews.as_view(), name='Actualizar'),
    path('ingresos_gastos/', Ingresos_GastosViews.as_view(), name='Listar'),
    path('ingresos_gastos/<int:nit>', Ingresos_GastosViews.as_view(), name='Actualizar'),
    path('login/', views.loginusuario, name='Login Usuario'),
    path('gestionadmin/',views.gestionadmin, name="gestion" ),
    path('formulario/', views.formularioregistro, name="Registro"), 
    path('formulario_empleado/', views.formularioregistroempleado, name="Registro"),
    path('formulario_usuario/', views.formularioregistrousuario, name="Registro"),
    path('formulario_ing-gastos/', views.formularioregistroingresosgastos, name="Registro"),
    path('gestionempleado/',views.gestionempleado, name="gestion" ),
    path('actualizarempresa/<int:nit>',views.actualizarempresa, name='frmact'),
    path('actualizarempresa/', views.actempresa, name="actualizar"),
    path('actualizarempleado/<int:identificacion>',views.actualizarempleado, name='frmact'),
    path('actualizarempleado/', views.actempleado, name="actualizar"),
    path('actualizarusuario/<str:nombre_usuario>',views.actualizarusuario, name='frmact'),
    path('actualizarusuario/', views.actusuario, name="actualizar"),
    path('eliminarusuario/<str:nombre_usuario>', views.eliminarusuario, name="eliminar"),
    path('consultardatosingresos_gastos/<int:nit>', views.consultarjoin, name="Consultar")
]