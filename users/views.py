from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from users.models import CustomUser
from apartments.models import Apartments
from payments.models import Payments
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from users.forms import CustomUserCreationForm, CustomUserUpdateForm


class CustomUserIndexView(ListView):
    model = CustomUser
    template_name = 'index.html'
    context_object_name = 'rantier_list'

class CustomUserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    context_object_name = 'rantier'
    template_name = 'user_detail.html'

    # def get_queryset(self, **kwargs):
    #     queryset = CustomUser.objects.filter(pk=self.kwargs['pk'])
    #     return queryset


class CustomUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('users:login')


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'user_update.html'