from django.db import models
from django.urls import reverse
from apartments.models import Apartments
from tenants.models import Tenants
from datetime import datetime, timedelta



class Contracts(models.Model):
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE, related_name='contracts')
    concluded_at = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
    # payment_period = models.IntegerField()  # field for more flex payment auto-creation (set timedelta value from this field)
    cost = models.IntegerField()
    tenant = models.ForeignKey(Tenants, on_delete=models.CASCADE, verbose_name='tenant name')

    def __str__(self):
        return f'Contract for apartment: {self.apartment} concluded at: {self.concluded_at}'

    # def get_absolute_url(self):
    #     return reverse('contracts:contract_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        """
        Override class method for auto-creation first payment with new contract
        :param args:
        :param kwargs:
        :return: None
        """
        from payments.models import Payments
        super().save(*args, **kwargs)
        Payments.objects.create(
            contract=self,
            description='Pay needed',
            rent_payment=self.cost,
            created_at=self.concluded_at + timedelta(30)
            # created_at=self.concluded_at + timedelta(self.payment_period)  # more flex behavior!!
        )
