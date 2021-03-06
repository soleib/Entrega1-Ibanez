import email
from threading import local
from urllib import request
import webbrowser
from xml.etree.ElementTree import QName
from django import views
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Avatar, Hamburguesas, Locales
from .forms import HamburguesaFormulario, UserEditForm   

from .models import Hamburguesas, Locales
from .forms import HamburguesaFormulario, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from.forms import ContactoForm


from django.views.generic import ListView,View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


# Create your views here.
def nosotros(request):
    if request.user.is_authenticated:
        if Avatar.objects.filter(user=request.user.id).exists():
            avatar= Avatar.objects.get(user=request.user.id)
            return render(request, 'nosotros.html',{'avatar':avatar})                          
        return render(request, 'nosotros.html') 
    if not request.user.is_authenticated:
        return render(request, 'nosotros.html')
       # return render(request, 'nosotros.html')
    
def inicio(request):
    if request.user.is_authenticated:
        if Avatar.objects.filter(user=request.user.id).exists():
            avatar= Avatar.objects.get(user=request.user.id)
            return render(request, 'inicio.html',{'avatar':avatar})                          
        return render(request, 'inicio.html') 
    if not request.user.is_authenticated:
        return render(request, 'inicio.html')

def hamburguesas(request):
    if request.user.is_authenticated:
        if Avatar.objects.filter(user=request.user.id).exists():
            avatar= Avatar.objects.get(user=request.user.id)
            return render(request, 'hamburguesas.html',{'avatar':avatar})                          
        return render(request, 'hamburguesas.html') 
    if not request.user.is_authenticated:
        return render(request, 'hamburguesas.html')


class formulariocontacto(LoginRequiredMixin,View):
 


    def get (self,request,*args,**kwargs):
        form=ContactoForm()
        contexto={
            'form':form
        }
        
        return render(request, 'contacto.html',contexto)

    def post(self,request,*args,**kwargs):
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'contactoRespuesta.html')
        else:
            contexto = {
                'form':form,
            }
            return render(request,'contacto.html',contexto)


              
@login_required
def comentarios(request):
    if request.user.is_authenticated:
        if Avatar.objects.filter(user=request.user.id).exists():
            avatar= Avatar.objects.get(user=request.user.id)
            return render(request, 'comentarios,html',{'avatar':avatar})                          
        return render(request, 'comentarios,html') 
    if not request.user.is_authenticated:
        return render(request, 'comentarios,html')
    
 

def locales(request):
    if request.user.is_authenticated:
        if Avatar.objects.filter(user=request.user.id).exists():
            avatar= Avatar.objects.get(user=request.user.id)
            return render(request, 'locales.html',{'avatar':avatar})                          
        return render(request, 'locales.html') 
    if not request.user.is_authenticated:
        return render(request, 'locales.html')
   

def agregalocal(request, nombrelocal, ciudad, provincia, direccion, altura, fechaapertura):

    tienda = Locales(nombrelocal=nombrelocal, ciudad=ciudad, provincia=provincia, direccion=direccion,altura=altura, fechaapertura=fechaapertura)
    tienda.save()
    return render(request, 'agregafamiliar.html', {'nombrelocal': nombrelocal,'ciudad': ciudad, 'provincia': provincia,'direccion': direccion, 'altura': altura, 'fechaapertura': fechaapertura})


def hamburguesaFormulario(request):
    if request.method == "POST":
        miFormulario = HamburguesaFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            hamburguesa = Hamburguesas(nombrehamburguesa = informacion['nombrehamburguesa'], tipopan = informacion['tipopan'], tipocarne = informacion['tipocarne'], cantidadmedallones = informacion['cantidadmedallones'], aderezo = informacion['aderezo'], salsaMrBlack = informacion["salsaMrBlack"], fechacreacion = informacion['fechacreacion'])
            hamburguesa.save()
            return render(request, "inicio.html")
    else:
        miFormulario = HamburguesaFormulario()
        return render(request, 'HamburguesaFormulario.html', {'miFormulario':miFormulario})

# def busquedalocal(request):
#     return render(request, "busquedaLocal.html")

# def buscar(request):
#     if request.GET["nombrelocal"]:
#         nombrelocal = request.GET["nombrelocal"]
#         locales = Locales.objects.filter(nombrelocal = nombrelocal)

#         return render(request, "resultadoBusqueda.html", {"locales":locales,"nombrelocal" : nombrelocal })
#     else:
#         return HttpResponse("No enviaste Datos")


def leerHamburguesas(request):
    hamburguesa= Hamburguesas.objects.all()
    contexto={"lista_hamburguesa":hamburguesa}
    return render(request,'leerhamburguesas.html',contexto)


def eliminar_hamburguesa(request,id):
    hamburguesa=Hamburguesas.objects.get(id=id)
    hamburguesa.delete()

    hamburguesa= Hamburguesas.objects.all()
    contexto={"lista_hamburguesa":hamburguesa}
    return render(request,'leerhamburguesas.html',contexto)

def editar_hamburguesa(request,id):
    hamburguesa=Hamburguesas.objects.get(id=id)

    if request.method == "POST":
        miFormulario=HamburguesaFormulario(request.POST)

        if miFormulario.is_valid():
            imformacion=miFormulario.cleaned_data

            hamburguesa.nombrehamburguesa=imformacion['nombrehamburguesa']
            hamburguesa.tipopan=imformacion['tipopan']
            hamburguesa.tipocarne=imformacion['tipocarne']
            hamburguesa.cantidadmedallones=imformacion['cantidadmedallones']
            hamburguesa.aderezo=imformacion['aderezo']
            hamburguesa.salsaMrBlack=imformacion['salsaMrBlack']
            hamburguesa.fechacreacion=imformacion['fechacreacion']

            hamburguesa.save()

            return render(request,'inicio.html')

    else:
        miFormulario=HamburguesaFormulario(
            initial={
                'nombrehamburguesa':hamburguesa.nombrehamburguesa,
                'tipopan':hamburguesa.tipopan,
                'tipocarne':hamburguesa.tipocarne,
                'cantidadmedallones':hamburguesa.cantidadmedallones,
                'aderezo':hamburguesa.aderezo,
                'salsaMrBlack':hamburguesa.salsaMrBlack,
                'fechacreacion':hamburguesa.fechacreacion})

    return render(request,'editarHamburguesa.html',{"miFormulario":miFormulario,"hamburguesa_nombre":hamburguesa.nombrehamburguesa})


class HamburguesaList(ListView):

      
      model = Hamburguesas
      template_name = "hamburguesas_list.html"
   



class HamburguesaDetalle(DetailView):

      model = Hamburguesas
      template_name = "hamburguesas_detalle.html"



class HamburguesaCreacion(PermissionRequiredMixin, CreateView):

      model = Hamburguesas
      template_name="hamburguesas_form.html"
      success_url = "/AppMrBlack/hamburguesas/list"
      fields = ['nombrehamburguesa','tipopan','tipocarne','cantidadmedallones','aderezo','salsaMrBlack','fechacreacion']
      permission_required='AppMrBlack.add_Hamburguesas'


class HamburguesaUpdate(PermissionRequiredMixin, UpdateView):

      model = Hamburguesas
      template_name="hamburguesas_form.html"
      success_url = "/AppMrBlack/hamburguesas/list"
      fields  = ['nombrehamburguesa','tipopan','tipocarne','cantidadmedallones','aderezo','salsaMrBlack','fechacreacion']
      permission_required='AppMrBlack.change_Hamburguesas'

class HamburguesaoDelete(PermissionRequiredMixin, DeleteView):

      model = Hamburguesas
      template_name="hamburguesas_confirm_delete.html"
      success_url = "/AppMrBlack/hamburguesas/list"
      permission_required='AppMrBlack.delete_Hamburguesas'
      

def login_request(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            psw = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=psw)

            if user is not None:
                login(request,user)
                if Avatar.objects.filter(user=request.user.id).exists():
                    avatar = Avatar.objects.get(user=request.user.id)                
                    return render(request, 'inicio.html', {"mensaje":f"Bienvenidx {usuario}", 'avatar':avatar} )
                return render(request, 'inicio.html', {"mensaje":f"Bienvenidx {usuario}"} )
            else:
                return render(request, 'inicio.html', {"mensaje":"Error, los datos ingresados son incorrectos"} )
        else:
                return render(request, 'inicio.html', {"mensaje":"Error, formulario incorrecto"} )
    form = AuthenticationForm()

    return render(request, 'login.html',{'form':form})

def register(request):
    if request.method =="POST":

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            form.save()
            return render(request, 'inicio.html',{'mensaje':'Usuario creado con ??xito'})
        
    else: 
        form = UserRegisterForm()
    return render(request, 'registro.html', {'form':form})

def busquedaHamburguesa(request):
    return render(request, "busquedaHamburguesa.html")

def buscarHamburguesa(request):
    if request.GET["nombrehamburguesa"]:
        nombrehamburguesa = request.GET["nombrehamburguesa"]
        if Hamburguesas.objects.filter(nombrehamburguesa =nombrehamburguesa).exists():
            hamburguesa = Hamburguesas.objects.filter(nombrehamburguesa =nombrehamburguesa)
            return render(request, "buscarHamburguesa.html", {"hamburguesa":hamburguesa,"nombrehamburguesa" : nombrehamburguesa})
        return HttpResponse("Los datos son incorrectos")
    else:
        return HttpResponse("No enviaste Datos")    

@login_required
def editarPerfil(request):

    #Instancia de login
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            #Datos que se modificar??n
            usuario.nombre = informacion['nombre']
            usuario.descripcion = informacion['descripcion']
            usuario.web = informacion['web']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.imagen = informacion['imagen']

            return render(request,"inicio.html") 
        #En caso de que no sea post
    else:
        #Creo el formulario con los datos que voy a modificar
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "editarPerfil.html",{"miFormulario":miFormulario, "usuario":usuario})

            
class LocalList(ListView):
      
    model = Locales
    template_name = "local_list.html"

    
  
class LocalDetalle(DetailView):

     model = Locales
     template_name = "local_detalle.html"



class LocalCreacion(PermissionRequiredMixin, CreateView):

    model = Locales
    template_name="local_form.html"
    success_url = "/AppMrBlack/local/list"
    fields = ['nombrelocal','ciudad','provincia','direccion','altura','fechaapertura']
    permission_required='AppMrBlack.add_Locales'

class LocalUpdate(PermissionRequiredMixin, UpdateView):
    model = Locales
    template_name="local_form.html"
    success_url = "/AppMrBlack/local/list"
    fields  = ['nombrelocal','ciudad','provincia','direccion','altura','fechaapertura']
    permission_required='AppMrBlack.change_Locales'

class LocalDelete(PermissionRequiredMixin, DeleteView):
    model = Locales
    template_name="local_confirm_delete.html"
    success_url = "/AppMrBlack/local/list"
    permission_required='AppMrBlack.delete_Locales'
