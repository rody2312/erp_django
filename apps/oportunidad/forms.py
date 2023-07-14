from django import forms
from .models import Oportunidad


class OportunidadForm(forms.ModelForm):
    class Meta:
        model = Oportunidad
        fields = '__all__'
        labels = {
            'id_gestion_comercial': 'Gestion comercial',
            'id_cliente': 'Cliente',
            'id_proveedor': 'Proveedor',
            'nombre_contacto': 'Contacto',
            'area': 'Área',
            'alcance': 'Alcance',
            'fecha_inicio': 'Fecha de inicio',
            'fecha_termino': 'Fecha de termino',
            'monto_probable': 'Monto probable',
            'fecha_facturacion': 'Fecha de facturación',
            'probabilidad_a_oc': 'Probabilidad a OC',
            'observaciones': 'Observaciones',
        }
        widgets = {
            'id_gestion_comercial': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_cliente': forms.Select(attrs={'class': 'form-control'}),
            'id_proveedor': forms.Select(attrs={'class': 'form-control'}),
            'nombre_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.Select(attrs={'class': 'form-control'}),
            'alcance': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_termino': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'monto_probable': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_facturacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'probabilidad_a_oc': forms.NumberInput(attrs={'class': 'form-control'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['area'].widget.choices = [
            ('agua', 'Agua'),
            ('mineria', 'Minería'),
            ('azucar', 'Azúcar'),
            ('gas', 'Gas'),
            ('Oil & gas UP', 'Oil & Gas UP'),
            ('Oil & gas DP', 'Oil & Gas DP'),
            ('eolica', 'Eólica'),
            ('solar', 'Solar'),
        ]
