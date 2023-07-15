from django import forms
from .models import Cotizacion

class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = '__all__'
        labels = {
            'id_oportunidad': 'Oportunidad',
            'incoterm': 'Incoterm',
            'tipo_operacion': 'Tipo de Operación',
            'fecha_cotizacion': 'Fecha de Cotización',
            'moneda': 'Moneda',
            'tipo_cambio': 'Tipo de Cambio',
            'plazo_entrega': 'Plazo de Entrega',
        }
        widgets = {
            'id_oportunidad': forms.Select(attrs={'class': 'form-control'}),
            'incoterm': forms.Select(attrs={'class': 'form-control'}),
            'tipo_operacion': forms.Select(attrs={'class': 'form-control'}),
            'fecha_cotizacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'moneda': forms.Select(attrs={'class': 'form-control'}),
            'tipo_cambio': forms.NumberInput(attrs={'class': 'form-control'}),
            'plazo_entrega': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

        labels['tipo_cambio'] = 'Tipo de Cambio'
        widgets['tipo_cambio'] = forms.NumberInput(attrs={'class': 'form-control'})
