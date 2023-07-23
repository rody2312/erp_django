from django import forms
from .models import Cotizacion
from apps.oportunidad.models import Oportunidad

class CotizacionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CotizacionForm, self).__init__(*args, **kwargs)
        # Modificar el queryset para el campo id_oportunidad para que se muestre en orden descendente
        self.fields['id_oportunidad'].queryset = Oportunidad.objects.order_by('-id_oportunidad')

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
