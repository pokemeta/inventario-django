import django_filters
from django import forms
from django.db import models
from .models import Item 

class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ['n_oficialia','descripcion','modelo_i','lugar','funcionario']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                    'widget': forms.TextInput(attrs={'class': 'form-control'})
                },
            },
        }
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super().__init__(data, queryset, request=request, prefix=prefix)
        for f in self.filters.values():
            if isinstance(f, django_filters.ChoiceFilter):
                    f.extra.update({'widget': forms.Select(attrs={'class' : 'form-control'})})