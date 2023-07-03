from django import forms
from .models import Venta


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
        widgets = {
            'id_cotizacion': forms.Select(attrs={'class': 'form-control'}),
            'n_orden_compra': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_orden_compra': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'moneda': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_cambio': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_entrega_oc': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_facturacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'utilidad_esperada': forms.NumberInput(attrs={'class': 'form-control'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
        }
