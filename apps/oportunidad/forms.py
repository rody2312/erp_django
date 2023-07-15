from django import forms
from .models import Oportunidad


class OportunidadForm(forms.ModelForm):
    class Meta:
        model = Oportunidad
        fields = '__all__'
        widgets = {
            'id_gestion_comercial': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.Select(attrs={'class': 'form-control'}),
            'alcance': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_termino': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'monto_probable': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_facturacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'probabilidad_a_oc': forms.Select(attrs={'class': 'form-control'}),
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
        self.fields['probabilidad_a_oc'].widget.choices = [
            (10, '10'),
            (25, '25'),
            (50, '50'),
            (75, '75'),
            (90, '90'),
        ]
