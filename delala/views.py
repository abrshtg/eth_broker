from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Property


class PropertyListView(ListView):
    model = Property
    template_name = 'property_list.html'
    context_object_name = 'properties'


class PropertyDetailView(DetailView):
    model = Property
    template_name = 'property_detail.html'
    context_object_name = 'property'


class PropertyCreateView(CreateView):
    model = Property
    template_name = 'property_form.html'
    fields = ['property_name', 'address', 'price', 'property_type']
    success_url = reverse_lazy('property_list')


class PropertyUpdateView(UpdateView):
    model = Property
    template_name = 'property_form.html'
    fields = ['property_name', 'address', 'price', 'property_type']
    success_url = reverse_lazy('property_list')


class PropertyDeleteView(DeleteView):
    model = Property
    template_name = 'property_confirm_delete.html'
    success_url = reverse_lazy('property_list')
