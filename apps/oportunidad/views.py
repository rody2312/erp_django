from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Oportunidad
from .forms import OportunidadForm


def index(request):
    return render(request, 'index.html')


class OportunidadListView(ListView):
    model = Oportunidad
    template_name = 'oportunidad/oportunidad_list.html'


class OportunidadDetailView(DetailView):
    model = Oportunidad
    template_name = 'oportunidad/oportunidad_detail.html'


class OportunidadCreateView(CreateView):
    model = Oportunidad
    form_class = OportunidadForm
    template_name = 'oportunidad/oportunidad_form.html'
    success_url = reverse_lazy('oportunidad_list')

    def form_valid(self, form):
        # Guardar la nueva cotización
        self.object = form.save()

        # Redirigir a la lista de cotizaciones
        return redirect(self.success_url)


class OportunidadUpdateView(UpdateView):
    model = Oportunidad
    form_class = OportunidadForm
    template_name = 'oportunidad/oportunidad_form.html'
    success_url = reverse_lazy('oportunidad_list')

    def form_valid(self, form):
        # Guardar la nueva cotización
        self.object = form.save()

        # Redirigir a la lista de cotizaciones
        return redirect(self.success_url)


class OportunidadDeleteView(DeleteView):
    model = Oportunidad
    template_name = 'oportunidad/oportunidad_confirm_delete.html'
    success_url = reverse_lazy('oportunidad_list')
