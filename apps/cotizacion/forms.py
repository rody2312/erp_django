from django import forms
from .models import Cotizacion


class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = '__all__'
        widgets = {
            'id_oportunidad': forms.Select(attrs={'class': 'form-control'}),
            'id_incoterm': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_operacion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_cotizacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'moneda': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_cambio': forms.TextInput(attrs={'class': 'form-control'}),
            'plazo_entrega': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
