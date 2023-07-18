from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
        labels = {
            'id_cotizacion': 'Cotización',
            'n_orden_compra': 'Número de orden de compra',
            'fecha_orden_compra': 'Fecha Orden de Compra',
            'moneda': 'Moneda',
            'tipo_cambio': 'Tipo de cambio',
            'fecha_entrega_oc': 'Fecha entrega oc',
            'fecha_facturacion': 'Fecha facturación',
            'utilidad_esperada': 'Utilidad esperada',
            'observaciones': 'Observaciones',
        }
        widgets = {
            'id_cotizacion': forms.Select(attrs={'class': 'form-control'}),
            'n_orden_compra': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_orden_compra': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'moneda': forms.Select(attrs={'class': 'form-control'}),
            'tipo_cambio': forms.NumberInput(attrs={'class': 'form-control'}),  # Cambia a forms.NumberInput
            'fecha_entrega_oc': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_facturacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'utilidad_esperada': forms.NumberInput(attrs={'class': 'form-control'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
        }
