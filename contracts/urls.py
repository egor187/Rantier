from django.urls import path
from contracts.views import ContractDetailView

app_name = 'contracts'

urlpatterns = [
    path('<int:pk>/', ContractDetailView.as_view(), name='contract_detail')
]