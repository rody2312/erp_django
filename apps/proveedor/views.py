from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Proveedor
from .forms import ProveedorForm


class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'proveedor/proveedor_list.html'


class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = 'proveedor/proveedor_detail.html'


class ProveedorCreateView(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.success_url)


class ProveedorUpdateView(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.success_url)


class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'proveedor/proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedor_list')
