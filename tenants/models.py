from django.db import models
# from contracts.models import Contracts
# from payments.models import Payments
from django.urls import reverse


class Tenants(models.Model):
    name = models.CharField('tenant name', max_length=120)
    email = models.EmailField()
    # contract = models.ForeignKey(Contracts, on_delete=models.SET_NULL)
    # payments = models.ForeignKey(Payments, on_delete=models.SET_NULL)


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('tenants.views.TenantDetailView', args=[str(self.pk)])
