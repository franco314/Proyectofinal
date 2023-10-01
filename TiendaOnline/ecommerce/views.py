from django.shortcuts import render
from django.http import HttpResponse , HttpRequest
from .models import Mouses, Teclados, Monitores, Auriculares, SillasGamer
from .forms import MouseFormulario, TecladosFormulario, MonitoresFormulario, AuricularesFormulario, SillasGamerFormulario
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm
from django.contrib.auth.views import LogoutView


def incio (req):

    return render (req, "inicio.html")


def mouses (req):

    return render (req, "mouses.html")


def teclados (req):

    return render (req, "teclados.html")


def monitores (req):

    return render (req, "monitores.html")


def auriculares (req):

    return render (req, "auriculares.html")

def silas_gamer (req):

    return render (req, "sillas_gamer.html")


def articulo_agregado(req):

    return render (req, "articulo_Agregado.html")

def mouse_formulario (req: HttpRequest):

    print("method", req.method)
    print("post", req.POST)

    if req.method == "POST":

        miFormulario = MouseFormulario(req.POST)

        if miFormulario.is_valid():
            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            mouse = Mouses(articulo=data["articulo"], precio=data["precio"], stock=data["stock"])
            mouse.save()
            return render (req, "articulo_agregado.html", {"mensaje": "¡Articulo agregado con éxito!"})
        else:
            return render (req, "articulo_agregado.html", {"mensaje": "¡Formulario inválido!"})
        
    else:    
       
       miFormulario = MouseFormulario()
    
       return render(req, "mouse_formulario.html", {"miFormulario": miFormulario})


def teclado_formulario (req: HttpRequest):

    print("method", req.method)
    print("post", req.POST)

    if req.method == "POST":

        miFormulario = TecladosFormulario(req.POST)

        if miFormulario.is_valid():
            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            mouse = Teclados(articulo=data["articulo"], precio=data["precio"], stock=data["stock"])
            mouse.save()
            return render (req, "articulo_agregado.html", {"mensaje": "¡Articulo agregado con éxito!"})
        else:
            return render (req, "articulo_agregado.html", {"mensaje": "¡Formulario inválido!"})
        
    else:    
       
       miFormulario = TecladosFormulario()
    
       return render(req, "teclado_formulario.html", {"miFormulario": miFormulario})
    

def monitores_formulario (req: HttpRequest):

    print("method", req.method)
    print("post", req.POST)

    if req.method == "POST":

        miFormulario = MonitoresFormulario(req.POST)

        if miFormulario.is_valid():
            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            monitores = Monitores(articulo=data["articulo"], precio=data["precio"], stock=data["stock"])
            monitores.save()
            return render (req, "articulo_agregado.html", {"mensaje": "¡Articulo agregado con éxito!"})
        else:
            return render (req, "articulo_agregado.html", {"mensaje": "¡Formulario inválido!"})
        
    else:    
       
       miFormulario = MonitoresFormulario()
    
       return render(req, "monitores_formulario.html", {"miFormulario": miFormulario})
    

def auriculares_formulario (req: HttpRequest):

    print("method", req.method)
    print("post", req.POST)

    if req.method == "POST":

        miFormulario = AuricularesFormulario(req.POST)

        if miFormulario.is_valid():
            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            auriculares = Auriculares(articulo=data["articulo"], precio=data["precio"], stock=data["stock"])
            auriculares.save()
            return render (req, "articulo_agregado.html", {"mensaje": "¡Articulo agregado con éxito!"})
        else:
            return render (req, "articulo_agregado.html", {"mensaje": "¡Formulario inválido!"})
        
    else:    
       
       miFormulario = AuricularesFormulario()
    
       return render(req, "auriculares_formulario.html", {"miFormulario": miFormulario})
    

def sillasgamer_formulario (req: HttpRequest):

    print("method", req.method)
    print("post", req.POST)

    if req.method == "POST":

        miFormulario = SillasGamerFormulario(req.POST)

        if miFormulario.is_valid():
            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            sillasGamer = SillasGamer(articulo=data["articulo"], precio=data["precio"], stock=data["stock"])
            sillasGamer.save()
            return render (req, "articulo_agregado.html", {"mensaje": "¡Articulo agregado con éxito!"})
        else:
            return render (req, "articulo_agregado.html", {"mensaje": "¡Formulario inválido!"})
        
    else:    
       
       miFormulario = SillasGamerFormulario()
    
       return render(req, "sillasgamer_formulario.html", {"miFormulario": miFormulario})



def listaMonitores(req):

    monitores = Monitores.objects.all()

    return render(req, "lista_monitores.html", {"monitores": monitores})


def eliminaMonitor(req, id):

    if req.method == 'POST':

        monitor = Monitores.objects.get(id=id)
        monitor.delete()

        monitores = Monitores.objects.all()

    return render(req, "lista_monitores.html", {"monitores": monitores})



def editarMonitor(req, id):

    monitores = Monitores.objects.get(id=id)

    if req.method == "POST":

        miFormulario = MonitoresFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            monitores.articulo = data["articulo"]
            monitores.stock = data["stock"]
            monitores.precio = data["precio"]
            monitores.save()
            return render (req, "articulo_agregado.html", {"mensaje": "¡Articulo actualizado con éxito!"})
        else:
            return render (req, "articulo_agregado.html", {"mensaje": "¡Formulario inválido!"})
        
    else:    
       
       miFormulario = MonitoresFormulario(initial={
           "articulo": monitores.articulo,
           "precio": monitores.precio,
           "stock": monitores.stock,
       })
    
       return render(req, "editar_monitor.html", {"miFormulario": miFormulario, "id": monitores.id})


def listaMouses(req):

    mouses = Mouses.objects.all()

    return render(req, "lista_mouses.html", {"mouses": mouses})


def eliminaMouse(req, id):

    if req.method == 'POST':

        mouses = Mouses.objects.get(id=id)
        mouses.delete()

        mouses = Mouses.objects.all()

    return render(req, "lista_mouses.html", {"mouses": mouses})


def editarMouse(req, id):

    mouses = Mouses.objects.get(id=id)

    if req.method == "POST":

        miFormulario = MonitoresFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            mouses.articulo = data["articulo"]
            mouses.stock = data["stock"]
            mouses.precio = data["precio"]
            mouses.save()
            return render (req, "articulo_agregado.html", {"mensaje": "¡Articulo actualizado con éxito!"})
        else:
            return render (req, "articulo_agregado.html", {"mensaje": "¡Formulario inválido!"})
        
    else:    
       
       miFormulario = MonitoresFormulario(initial={
           "articulo": mouses.articulo,
           "precio": mouses.precio,
           "stock": mouses.stock,
       })
    
       return render(req, "editar_mouse.html", {"miFormulario": miFormulario, "id": mouses.id})
    


def listaAuriculares(req):

    auriculares = Auriculares.objects.all()

    return render(req, "lista_auriculares.html", {"auriculares": auriculares})


def eliminaAuricular(req, id):

    if req.method == 'POST':

        auriculares = Auriculares.objects.get(id=id)
        auriculares.delete()

        auriculares = Auriculares.objects.all()

    return render(req, "lista_auriculares.html", {"auriculares": auriculares})


def editarAuricular(req, id):

    auriculares = Auriculares.objects.get(id=id)

    if req.method == "POST":

        miFormulario = AuricularesFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            auriculares.articulo = data["articulo"]
            auriculares.stock = data["stock"]
            auriculares.precio = data["precio"]
            auriculares.save()
            return render (req, "articulo_agregado.html", {"mensaje": "¡Articulo actualizado con éxito!"})
        else:
            return render (req, "articulo_agregado.html", {"mensaje": "¡Formulario inválido!"})
        
    else:    
       
       miFormulario = MonitoresFormulario(initial={
           "articulo": auriculares.articulo,
           "precio": auriculares.precio,
           "stock": auriculares.stock,
       })
    
       return render(req, "editar_auriculares.html", {"miFormulario": miFormulario, "id": auriculares.id})
    


def listaTeclados(req):

    teclados = Teclados.objects.all()

    return render(req, "lista_teclados.html", {"teclados": teclados})


def eliminaTeclado(req, id):

    if req.method == 'POST':

        teclados = Teclados.objects.get(id=id)
        teclados.delete()

        teclados = Teclados.objects.all()

    return render(req, "lista_teclados.html", {"teclados": teclados})


def editarTeclado(req, id):

    teclados = Teclados.objects.get(id=id)

    if req.method == "POST":

        miFormulario = TecladosFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            teclados.articulo = data["articulo"]
            teclados.stock = data["stock"]
            teclados.precio = data["precio"]
            teclados.save()
            return render (req, "articulo_agregado.html", {"mensaje": "¡Articulo actualizado con éxito!"})
        else:
            return render (req, "articulo_agregado.html", {"mensaje": "¡Formulario inválido!"})
        
    else:    
       
       miFormulario = MonitoresFormulario(initial={
           "articulo": teclados.articulo,
           "precio": teclados.precio,
           "stock": teclados.stock,
       })
    
       return render(req, "editar_teclados.html", {"miFormulario": miFormulario, "id": teclados.id})



def listaSillas(req):

    sillas = SillasGamer.objects.all()

    return render(req, "lista_sillas.html", {"sillas": sillas})


def eliminaSillas(req, id):

    if req.method == 'POST':

        sillas = SillasGamer.objects.get(id=id)
        sillas.delete()

        sillas = SillasGamer.objects.all()

    return render(req, "lista_sillas.html", {"sillas": sillas})


def editarSillas(req, id):

    sillas = SillasGamer.objects.get(id=id)

    if req.method == "POST":

        miFormulario = SillasGamerFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            sillas.articulo = data["articulo"]
            sillas.stock = data["stock"]
            sillas.precio = data["precio"]
            sillas.save()
            return render (req, "articulo_agregado.html", {"mensaje": "¡Articulo actualizado con éxito!"})
        else:
            return render (req, "articulo_agregado.html", {"mensaje": "¡Formulario inválido!"})
        
    else:    
       
       miFormulario = SillasGamerFormulario(initial={
           "articulo": sillas.articulo,
           "precio": sillas.precio,
           "stock": sillas.stock,
       })
    
       return render(req, "editar_sillas.html", {"miFormulario": miFormulario, "id": sillas.id})
    


def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "inicio.html", {"mensaje": f"Bienvenido {usuario}"})

            else:
                return render(request, "inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})
   




def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"registro.html" ,  {"form":form})











class MouseList(ListView):
    model = Mouses
    template_name = "mouses_list.html"
    context_object_name = "mouses"



class MouseDetail(DetailView):
    model = Mouses
    template_name = "mouses_detail.html"
    context_object_name = "mouse"



class MouseCreate(CreateView):
    model = Mouses
    template_name = "mouses_create.html"
    fields = ["articulo", "precio", "stock"]
    success_url = "/ecommerce/lista_mouse" 



class MouseUpdate(UpdateView):
    model = Mouses
    template_name = "mouses_update.html"
    fields = ["articulo", "precio", "stock"]
    success_url = "/ecommerce/lista_mouse" 


class MouseDelete(DeleteView):
    model = Mouses
    template_name = "mouses_delete.html"
    success_url = "/ecommerce/lista_mouse" 




class TecladoList(ListView):
    model = Teclados
    template_name = "teclados_list.html"
    context_object_name = "teclados"



class TecladoDetail(DetailView):
    model = Teclados
    template_name = "teclados_detail.html"
    context_object_name = "teclado"



class TecladoCreate(CreateView):
    model = Teclados
    template_name = "teclados_create.html"
    fields = ["articulo", "precio", "stock"]
    success_url = "/ecommerce/list_teclados" 



class TecladoUpdate(UpdateView):
    model = Teclados
    template_name = "teclados_update.html"
    fields = ["articulo", "precio", "stock"]
    success_url = "/ecommerce/list_teclados" 


class TecladoDelete(DeleteView):
    model = Teclados
    template_name = "teclados_delete.html"
    success_url = "/ecommerce/list_teclados" 





class MonitoresList(ListView):
    model = Monitores
    template_name = "monitores_list.html"
    context_object_name = "monitores"



class MonitoresDetail(DetailView):
    model = Monitores
    template_name = "monitores_detail.html"
    context_object_name = "monitor"



class MonitoresCreate(CreateView):
    model = Monitores
    template_name = "monitores_create.html"
    fields = ["articulo", "precio", "stock"]
    success_url = "/ecommerce/monitores_list" 



class MonitoresUpdate(UpdateView):
    model = Monitores
    template_name = "monitores_update.html"
    fields = ["articulo", "precio", "stock"]
    success_url = "/ecommerce/monitores_list" 


class MonitoresDelete(DeleteView):
    model = Monitores
    template_name = "monitores_delete.html"
    success_url = "/ecommerce/monitores_list" 





class AuricularesList(ListView):
    model = Auriculares
    template_name = "auriculares_list.html"
    context_object_name = "auriculares"



class AuricularesDetail(DetailView):
    model = Auriculares
    template_name = "auriculares_detail.html"
    context_object_name = "auricular"



class AuricularesCreate(CreateView):
    model = Auriculares
    template_name = "auriculares_create.html"
    fields = ["articulo", "precio", "stock"]
    success_url = "/ecommerce/auriculares_list" 



class AuricularesUpdate(UpdateView):
    model = Auriculares
    template_name = "auriculares_update.html"
    fields = ["articulo", "precio", "stock"]
    success_url = "/ecommerce/auriculares_list" 


class AuricularesDelete(DeleteView):
    model = Auriculares
    template_name = "auriculares_delete.html"
    success_url = "/ecommerce/auriculares_list" 





class SillasGamerList(ListView):
    model = SillasGamer
    template_name = "sillasGamer_list.html"
    context_object_name = "sillas"



class SillasGamerDetail(DetailView):
    model = SillasGamer
    template_name = "sillasGamer_detail.html"
    context_object_name = "silla"



class SillasGamerCreate(CreateView):
    model = SillasGamer
    template_name = "sillasGamer_create.html"
    fields = ["articulo", "precio", "stock"]
    success_url = "/ecommerce/sillasGamer_list" 



class SillasGamerUpdate(UpdateView):
    model = SillasGamer
    template_name = "sillasGamer_update.html"
    fields = ["articulo", "precio", "stock"]
    success_url = "/ecommerce/sillasGamer_list" 
    context_object_name = "sillas"


class SillasGamerDelete(DeleteView):
    model = SillasGamer
    template_name = "sillasGamer_delete.html"
    success_url = "/ecommerce/sillasGamer_list" 




