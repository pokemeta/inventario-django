import django_filters
from django import forms
from django.db import models
from .models import Location

class LocationFilter(django_filters.FilterSet):
    class Meta:
        model = Location
        fields = ['name','description']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                    'widget': forms.TextInput(attrs={'class': 'form-control'})
                },
            },
        }