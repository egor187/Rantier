from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from users.models import CustomUser
from contracts.models import Contracts
from django.contrib import messages
from django.shortcuts import redirect
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

    not_allowed_message = "You can't see details about another rantier"
    redirect_url = reverse_lazy('users:user_index')

    def dispatch(self, request, *args, **kwargs):
        """
        Prohibit access to another rantiers detail page
        """
        if self.request.user.pk != kwargs['pk']:
            messages.error(request, self.not_allowed_message)
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Add Contract instance to context
        :param kwargs:
        :return: new 'key/value' pair in context dict
        """
        context = super().get_context_data()

        # filtering model instance to url_dispatcher kwarg from url
        context['contract'] = Contracts.objects.filter(apartment__owner__pk=self.kwargs['pk'])

        # Another realization: return contracts filtered by current user in session
        # from self.request (more secured). Useless with overriden dispatch super-class merhod
        # context['contract'] = Contracts.objects.filter(apartment__owner__pk=self.request.user.pk)
        return context


class CustomUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('users:login')


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'user_update.html'