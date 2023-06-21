from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Venta
from .forms import VentaForm

class VentaListView(ListView):
    model = Venta
    template_name = 'venta/venta_list.html'

class VentaDetailView(DetailView):
    model = Venta
    template_name = 'venta/venta_detail.html'

class VentaCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'venta/venta_form.html'

class VentaUpdateView(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'venta/venta_form.html'

class VentaDeleteView(DeleteView):
    model = Venta
    template_name = 'venta/venta_confirm_delete.html'
    success_url = reverse_lazy('venta_list')
