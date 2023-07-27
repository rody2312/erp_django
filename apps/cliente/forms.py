from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    def clean_nombre_cliente(self):
        nombre_cliente = self.cleaned_data.get('nombre_cliente')
        if not nombre_cliente.isalpha():
            raise forms.ValidationError("El nombre debe contener solo letras.")
        return nombre_cliente

    def clean_localidad_cliente(self):
        localidad_cliente = self.cleaned_data.get('localidad_cliente')
        if not localidad_cliente.isalpha():
            raise forms.ValidationError(
                "La localidad debe contener solo letras.")
        return localidad_cliente

    class Meta:
        model = Cliente
        fields = '__all__'
        labels = {
            'nombre_cliente': 'Nombre de cliente',
            'direccion_cliente': 'Direccion de cliente',
            'codigo_postal_cliente': 'Codigo postal',
            'localidad_cliente': 'Localidad',
            'pais_cliente': 'Pais',
            'telefono_cliente': 'Telefono',
            'correo_cliente': 'Correo',
            'area_cliente': 'Area',
            'observaciones_cliente': 'Observaciones',
        }
        widgets = {
            'id_cliente': forms.Select(attrs={'class': 'form-control'}),
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_postal_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'localidad_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'pais_cliente': forms.Select(attrs={'class': 'form-control'}),
            'telefono_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_cliente': forms.EmailInput(attrs={'class': 'form-control'}),
            'area_cliente': forms.Select(attrs={'class': 'form-control'}),
            'observaciones_cliente': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 10%;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pais_cliente'].choices = [
            ('AR', 'Argentina'),
            ('BR', 'Brasil'),
            ('CL', 'Chile'),
            ('CO', 'Colombia'),
            ('MX', 'México'),
            ('PE', 'Perú'),
        ]
        self.fields['area_cliente'].widget.choices = [
            ('agua', 'Agua'),
            ('mineria', 'Minería'),
            ('azucar', 'Azúcar'),
            ('gas', 'Gas'),
            ('Oil & gas UP', 'Oil & Gas UP'),
            ('Oil & gas DP', 'Oil & Gas DP'),
            ('eolica', 'Eólica'),
            ('solar', 'Solar'),
        ]
