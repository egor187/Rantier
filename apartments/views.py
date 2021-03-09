from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from apartments.models import Apartments
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ApartmentsIndexView(ListView):
    model = Apartments
    template_name = 'apartment_index.html'
    context_object_name = 'apartments_list'

    def get_queryset(self):
        queryset = Apartments.objects.filter(owner__pk = self.request.user.pk)
        return queryset


class ApartmentsDetailView(DetailView):
    model = Apartments
    template_name = 'apartment_detail.html'
    context_object_name = 'apartment'


class ApartmentsUpdateView(UpdateView):
    model = Apartments
    fields = '__all__'
    template_name = 'apartment_update.html'


class ApartmentsCreateView(LoginRequiredMixin, CreateView):
    model = Apartments
    fields = [
        'current_tenant',
        'address',
        'size',
    ]
    template_name = 'apartment_create.html'
    success_url = reverse_lazy('apartments:apartment_index')

    # override class-method to achieve auto increment form field
    # "owner" with current autheticated user
    def form_valid(self, form):
        # attribute "user" contain current login user by LoginRequiredMixin
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ApartmentsDeleteView(DeleteView):
    model = Apartments
    context_object_name = 'apartment'
    template_name = 'apartment_delete.html'