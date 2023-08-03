from django import forms
from .models import Item

class DateInput(forms.DateInput):
    input_type = 'date'
class SelectInput(forms.Select):
    input_type = 'Select'


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['n_oficialia','descripcion','n_serie','marca','modelo_i','f_factura','n_factura','orden_c','proveedor_c','centro_c','comentarios','lugar','funcionario']
        widgets = {
            'n_oficialia': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe el numero de oficialia'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe el nombre del bien.'}),
            'n_serie': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Número de serie del bien.'}),
            'marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe la marca.'}),
            'modelo_i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe el modelo'}),
            'f_factura': DateInput(attrs={'class':'form-control',}),
            'n_factura': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe el nombre del bien.'}),
            'orden_c': forms.TextInput(attrs={'class':'form-control','placeholder':'Número de orden de compra'}),
            'proveedor_c': forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe el proveedor'}),
            'centro_c': forms.TextInput(attrs={'class':'form-control','placeholder':'Centro de no se que'}),
            'comentarios': forms.Textarea(attrs={'class':'form-control','placeholder':'Escribe los comentarios'}),
            'lugar': forms.Select(attrs={'class':'form-control',}),
            'funcionario': forms.Select(attrs={'class':'form-control',}),
        }

class ItemFormLugar(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['lugar',]
        widgets = {
            'lugar': forms.Select(attrs={'class':'form-control',}),
        }