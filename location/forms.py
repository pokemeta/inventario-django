from django import forms
from .models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name','description']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del área'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripción corta..'}),
        }