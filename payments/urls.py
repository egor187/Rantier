from django.urls import path
from payments.views import PaymentDetailView, PaymentCreateView


app_name = 'payments'

urlpatterns = [
    path('<int:pk>/', PaymentDetailView.as_view(), name='payment_detail'),
    path('create/', PaymentCreateView.as_view(), name='payment_create'),
]