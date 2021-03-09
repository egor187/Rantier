from django.shortcuts import render
from payments.models import Payments
from django.views.generic import DetailView


class PaymentDetailView(DetailView):
    model = Payments
    template_name = 'payment_detail.html'
    context_object_name = 'payment'
