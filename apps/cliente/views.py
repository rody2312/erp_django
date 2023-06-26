from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente


class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'
    context_object_name = 'cliente'


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cliente_create.html'
    fields = '__all__'


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'cliente_update.html'
    fields = '__all__'


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    success_url = '/cliente/'  # URL a la que se redirige después de eliminar un cliente
