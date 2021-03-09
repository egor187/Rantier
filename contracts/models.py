from django.db import models
from django.urls import reverse
from apartments.models import Apartments
from tenants.models import Tenants


class Contracts(models.Model):
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE, related_name='contracts')
    concluded_at = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
    cost = models.IntegerField()
    tenant = models.ForeignKey(Tenants, on_delete=models.CASCADE, verbose_name='tenant name')

    def __str__(self):
        return f'Contract for apartment: {self.apartment} concluded at: {self.concluded_at}'

    # def get_absolute_url(self):
    #     return reverse('contracts:contract_detail', args=[str(self.id)])