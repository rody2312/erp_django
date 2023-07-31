from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Venta
from .forms import VentaForm


class VentaListView(ListView):
    model = Venta
    template_name = 'venta/venta_list.html'
    context_object_name = 'venta_list'

def get_queryset(self):
    return Venta.objects.order_by('-id_venta')  # El '-' indica orden descendente

class VentaDetailView(DetailView):
    model = Venta
    template_name = 'venta/venta_detail.html'


class VentaCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'venta/venta_form.html'
    success_url = reverse_lazy('venta_list')

    def form_valid(self, form):
        # Guardar la nueva venta
        self.object = form.save()

        # Redirigir a la lista de ventas
        return redirect(self.success_url)


class VentaUpdateView(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'venta/venta_form.html'
    # Actualiza la URL de redirección aquí
    success_url = reverse_lazy('venta_list')


class VentaDeleteView(DeleteView):
    model = Venta
    template_name = 'venta/venta_confirm_delete.html'
    success_url = reverse_lazy('venta_list')
