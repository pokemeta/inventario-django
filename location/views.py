from django.shortcuts import render, redirect, get_object_or_404
from .models import Location
from .forms import LocationForm
from django.contrib.auth.decorators import login_required, permission_required    # son restricciones al metodo por parte del frame 
from .filters import LocationFilter
from django.core.paginator import Paginator
# Create your views here.
@login_required
@permission_required('is_staff', 'error_perm')
def list_location(request):
    location_filter = LocationFilter(request.GET, Location.objects.all() )
    pagination = Paginator(location_filter.qs,15)
    page = request.GET.get('page')
    locations = pagination.get_page(page)
    number_pages = "a"*locations.paginator.num_pages
    return render(request, 'location/list.html', {
        'locations':locations,
        'location_filter':location_filter,
        'nums': number_pages,
    })
@login_required
@permission_required('is_staff', 'error_perm')
def create_location(request):
    if request.method == 'GET':
        return render(request,'location/form_location.html',{
            'form':LocationForm,
            'form_action':'create',
        })
    else:
        try:
            form = LocationForm(request.POST)
            form.save()
            return redirect('list_location')
        except ValueError:
            return render(request,'location/form_location.html',{
                'form':LocationForm,
                'form_action':'create',
                'error':'Porfavor introdusca los datos correctos'
            })
@login_required
@permission_required('is_staff', 'error_perm')
def update_location(request, location_id):
    if request.method == 'GET':
        location = get_object_or_404(Location, pk=location_id)
        form = LocationForm(instance=location)
        return render(request,'location/form_location.html',{
            'location':location,
            'form':form,
            'form_action':'update'
        })
    else:
        try:
            location = get_object_or_404(Location,pk=location_id)
            form = LocationForm(request.POST,instance=location)
            form.save()
            return redirect('list_location')
        except ValueError:
            return render(request,'location/form_location.html',{
                'location':location,
                'form':form,
                'form_action':'update',
                'error': 'Porfavor introduce los datos correctos'
            })