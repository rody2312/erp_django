from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'id_cliente': forms.Select(attrs={'class': 'form-control'}),
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_postal_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'localidad_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'pais_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_cliente': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo_cliente': forms.EmailInput(attrs={'class': 'form-control'}),
            'area_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones_cliente': forms.Textarea(attrs={'class': 'form-control'}),
        }
