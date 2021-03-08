from django.db import models
from contracts.models import Contracts


class Payments(models.Model):
    # apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE, null=True)
    contract = models.ForeignKey(Contracts, on_delete=models.PROTECT)
    description = models.CharField(max_length=220, blank=True)
    rent_payment = models.IntegerField('rent payment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Payment for contract about apartment: {self.contract.apartment} from tenant: {self.contract.tenant}'
