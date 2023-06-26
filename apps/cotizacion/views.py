from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Cotizacion
from .forms import CotizacionForm


class CotizacionListView(ListView):
    model = Cotizacion
    template_name = 'cotizacion/cotizacion_list.html'


class CotizacionDetailView(DetailView):
    model = Cotizacion
    template_name = 'cotizacion/cotizacion_detail.html'


class CotizacionCreateView(CreateView):
    model = Cotizacion
    form_class = CotizacionForm
    template_name = 'cotizacion/cotizacion_form.html'
    success_url = reverse_lazy('cotizacion_list')

    def form_valid(self, form):
        # Guardar la nueva cotización
        self.object = form.save()

        # Redirigir a la lista de cotizaciones
        return redirect(self.success_url)


class CotizacionUpdateView(UpdateView):
    model = Cotizacion
    form_class = CotizacionForm
    template_name = 'cotizacion/cotizacion_form.html'


class CotizacionDeleteView(DeleteView):
    model = Cotizacion
    template_name = 'cotizacion/cotizacion_confirm_delete.html'
    success_url = reverse_lazy('cotizacion_list')
