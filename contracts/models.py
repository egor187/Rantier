from django.db import models
from django.urls import reverse
from apartments.models import Apartments
from tenants.models import Tenants
from users.models import CustomUser


# class Contracts(models.Model):
#     apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE, related_name='apartment')
#     concluded_at = models.DateField(auto_now_add=True)
#     expiration_date = models.DateField()
#     owner = models.ForeignKey(Apartments, on_delete=models.CASCADE, to_field='owner', related_name='owner')
#     tenant = models.ForeignKey(Tenants, on_delete=models.CASCADE, verbose_name='tenant name')
#
#     def __str__(self):
#         return self.concluded_at
#
#     def get_absolute_url(self):
#         return reverse('contracts.views.ContractsDetailView', args=[str(self.id)])