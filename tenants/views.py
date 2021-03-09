from django.shortcuts import render
from tenants.models import Tenants
from tenants.forms import TenantCreateForm, TenantUpdateForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView


def tenants_index_view(request):
    query_set = Tenants.objects.all()
    context = {'tenants': query_set}
    return render(request, 'tenant_index.html', context)


def tenant_create_view(request):
    if request.method == 'POST':
        form = TenantCreateForm(request.POST)
        if form.is_valid():
            Tenants.objects.create(name=form.cleaned_data['name'], email=form.cleaned_data['email'])
            return HttpResponseRedirect(reverse_lazy('tenants:tenant_index'))
    else:
        form = TenantCreateForm(initial={'name': request.user, 'email': request.user.email})
    return render(request, 'tenant_create.html', {'form': form})


# MORE INTUITIVELY realization with built-in class-based view for create instance of a model (CreateView)
# class TenantCreateView(CreateView):
#     model = Tenants
#     template_name = 'tenant_create.html'
#     form_class = TenantCreateForm
#     success_url = reverse_lazy('tenants:tenant_index')


class TenantDetailView(DetailView):
    model = Tenants
    template_name = 'tenant_detail.html'
    context_object_name = 'tenant'


class TenantUpdateView(LoginRequiredMixin, UpdateView):
    model = Tenants
    form_class = TenantUpdateForm
    template_name = 'tenant_update.html'
    context_object_name = 'tenant'


class TenantDeleteView(LoginRequiredMixin, DeleteView):
    model = Tenants
    success_url = reverse_lazy('tenants:tenant_index')
    context_object_name = 'tenant'
    template_name = 'tenant_delete.html'
