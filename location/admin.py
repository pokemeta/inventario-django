from django.contrib import admin
from .models import Location
# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    readonly_fields=['created_at','updated_at']

admin.site.register(Location,LocationAdmin)