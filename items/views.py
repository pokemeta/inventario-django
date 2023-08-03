from django.shortcuts import render, get_object_or_404,redirect
from .models import Item
from .forms import ItemForm, ItemFormLugar
from django.contrib.auth.forms import AuthenticationForm # Usar el formulario de usuario inicio de sesión
from django.contrib.auth import login, logout, authenticate  # metodos de django del apartado usuario
from django.contrib.auth.decorators import login_required, permission_required    # son restricciones al metodo por parte del frame 
from .filters import ItemFilter
from django.core.paginator import Paginator
# Create your views here.
#----------------------------------------------------------------------------------------------------------------------------------------------Por funcionario
def home(request):
    return render(request,'home.html')
#----------------------------------- sirve para mandar a una vista de error
def error_perm(request):
    return render(request,'user/error_miss.html')
#---------------------------------------------------------------------------------Listado de inventario 
@login_required
def list_items(request):
    item_filter = ItemFilter(request.GET,Item.objects.filter(active=True, funcionario= request.user))
    pagination = Paginator(item_filter.qs,10)
    page = request.GET.get('page')
    items = pagination.get_page(page)
    number_pages = "a"*items.paginator.num_pages
    return render(request,'item/list.html',{
        'items':items,
        'item_filter':item_filter,
        'nums': number_pages,
    })
#--------------------------------------------------------------------------------Detalle de item
@login_required
def item_detail(request,item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item/item_detail.html',{
        'item':item,
        'form':ItemForm,
    })
#-------------------------------------------------------------------------------Actualizar Lugar
@login_required
def updated_location(request, item_id):
    if request.method=='GET':
        item = get_object_or_404(Item,pk=item_id)
        form = ItemFormLugar(instance=item)
        return render(request,'item/item_ulocation.html',{
            'item':item,
            'form':form
        })
    else:
        try:
            item = get_object_or_404(Item, pk=item_id)
            form = ItemFormLugar(request.POST, instance=item)
            form.save()
            return redirect('item_detail',item_id)
        except ValueError:
            return render(request,'item/item_ulocation.html',{
                'item':item,
                'form':form,
                'error':'A surgido un error!!'
            })
#----------------------------------------------------------------------------------------------------------------------------------------------------Usuario

def sigin(request):
    if request.method=='GET':
        return render(request,'user/login.html',{
            'form':AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'user/login.html',{
                'form':AuthenticationForm,
                'error':'El usuario o las credenciales no son correctas'
            })
        else:
            login(request,user)
            return redirect('list_items')
#------------------------------------------- cerrar sesión
@login_required
def singout(request):
    logout(request)
    return redirect('home')



#------------------------------------------------------------------------------------------------------------------------------------------- Administrador de bienes
@permission_required('is_staff', 'error_perm') #----- el segundo parametro es para mandar una vista de error
def list_items_all(request):
    item_filter = ItemFilter(request.GET,Item.objects.filter(active=True))
    pagination = Paginator(item_filter.qs,10)
    page = request.GET.get('page')
    items = pagination.get_page(page)
    number_pages = "a"*items.paginator.num_pages
    return render(request,'item/list_all.html',{
        'items':items,
        'item_filter':item_filter,
        'nums': number_pages,
    })
    
@permission_required('is_staff', 'error_perm')
def create_item(request):
    if request.method=='GET':
        return render(request,'item/form_item.html',{
            'form': ItemForm,
            'form_action':'create',
        })
    else:
        try:
            form = ItemForm(request.POST)
            form.save()
            return redirect('list_items_all')
        except ValueError:
             return render(request,'item/form_item.html',{
                'form': ItemForm,
                'form_action':'create',
                'error': 'Introduce los datos correctos',
            })
@permission_required('is_staff', 'error_perm')
def updated_item(request, item_id):
    if request.method=='GET':
        item = get_object_or_404(Item,pk=item_id)
        form = ItemForm(instance=item)
        return render(request,'item/form_item.html',{
            'item':item,
            'form':form,
            'form_action':'update'
        })
    else:
        try:
            item = get_object_or_404(Item, pk=item_id)
            form = ItemForm(request.POST, instance=item)
            form.save()
            return redirect('list_items_all',item_id)
        except ValueError:
            return render(request,'item/form_item.html',{
                'item':item,
                'form':form,
                'form_action':'update',
                'error':'A surgido un error!!'
            })