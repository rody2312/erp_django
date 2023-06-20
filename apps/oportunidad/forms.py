from django import forms
from .models import Oportunidad

class OportunidadForm(forms.ModelForm):
    class Meta:
        model = Oportunidad
        fields = '__all__'
        widgets = {
            'id_gestion_comercial': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_cliente': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_contacto': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_proveedor': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'alcance': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_termino': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'monto_probable': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_facturacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'probabilidad_a_oc': forms.NumberInput(attrs={'class': 'form-control'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
        }
