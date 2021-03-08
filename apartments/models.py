from django.db import models
from users.models import CustomUser
# from tenants.models import Tenants
from django.urls import reverse


class Apartments(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # current_tenant = models.ForeignKey(Tenants, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200)
    size = models.IntegerField()

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('apartments:apartment_detail', args=[str(self.id)])