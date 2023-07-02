from django import forms
from .models import Proveedor


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'id_proveedor': forms.Select(attrs={'class': 'form-control'}),
            'nombre_proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_postal_proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'localidad_proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'pais_proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_proveedor': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo_proveedor': forms.EmailInput(attrs={'class': 'form-control'}),
            'area_proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones_proveedor': forms.Textarea(attrs={'class': 'form-control'}),
        }
