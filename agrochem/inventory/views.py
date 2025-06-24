from django.views.generic import (ListView, CreateView, UpdateView, 
                                DeleteView, DetailView)
from django.urls import reverse_lazy
from .models import Chemical
from django.shortcuts import render
from .models import Chemical
from django.core.paginator import Paginator

class ChemicalListView(ListView):
    model = Chemical
    template_name = 'inventory/chemical_list.html'
    context_object_name = 'chemicals'
    paginate_by = 1000
    


class ChemicalCreateView(CreateView):
    model = Chemical
    fields = '__all__'
    template_name = 'inventory/chemical_form.html'
    success_url = reverse_lazy('inventory:chemical-list')

class ChemicalDetailView(DetailView):
    model = Chemical
    template_name = 'inventory/chemical_detail.html'
    context_object_name = 'chemical'

class ChemicalUpdateView(UpdateView):
    model = Chemical
    fields = '__all__'
    template_name = 'inventory/chemical_form.html'
    success_url = reverse_lazy('inventory:chemical-list')

class ChemicalDeleteView(DeleteView):
    model = Chemical
    template_name = 'inventory/chemical_confirm_delete.html'
    success_url = reverse_lazy('inventory:chemical-list')