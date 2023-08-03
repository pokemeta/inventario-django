"""inventario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from location import views as viewsLocation
from items import views as viewsItems

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewsItems.home, name='home'),
    path('error', viewsItems.error_perm, name='error_perm'),
    path('login/', viewsItems.sigin,name='login'),
    path('logout/',viewsItems.singout, name='logout'),
    path('list_items/',viewsItems.list_items, name='list_items'),
    path('all_items/',viewsItems.list_items_all, name='list_items_all'),
    path('item_detail/<int:item_id>/',viewsItems.item_detail, name='item_detail'),
    path('updated_location/<int:item_id>/',viewsItems.updated_location, name='updated_location'),
    path('create_item/',viewsItems.create_item,name='create_item'),
    path('update_item/<int:item_id>/',viewsItems.updated_item, name='updated_item'),
    path('location/list/', viewsLocation.list_location,name='list_location'),
    path('location/create/', viewsLocation.create_location, name='create_location'),
    path('location/update/<int:location_id>/',viewsLocation.update_location,name='update_location')
]
