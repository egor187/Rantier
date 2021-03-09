from django.shortcuts import render
from contracts.models import Contracts
from django.views.generic import DetailView


class ContractDetailView(DetailView):
    model = Contracts
    template_name = 'contract_detail.html'
    context_object_name = 'contract'