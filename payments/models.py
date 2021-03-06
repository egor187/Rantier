from django.db import models
from tenants.models import Tenants
from apartments.models import Apartments

# from contracts.models import Contracts

class Payments(models.Model):
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=220, blank=True)
    rent_payment = models.IntegerField('rent payment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
