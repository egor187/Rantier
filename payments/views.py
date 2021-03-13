from django.shortcuts import render
from payments.models import Payments
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from payments.forms import PaymentCreationForm


class PaymentDetailView(DetailView):
    model = Payments
    template_name = 'payment_detail.html'
    context_object_name = 'payment'


class PaymentCreateView(CreateView):
    model = Payments
    form_class = PaymentCreationForm
    template_name = 'payment_create.html'