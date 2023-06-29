from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm


class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente/cliente_detail.html'


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.success_url)


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

    def form_valid(self, form):
        # Guardar la nueva cotización
        self.object = form.save()

        # Redirigir a la lista de cotizaciones
        return redirect(self.success_url)


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')
