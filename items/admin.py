from django.contrib import admin
from .models import Item
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    readonly_fields=['created_at','updated_at']

admin.site.register(Item,ItemAdmin)