from django.db import models
from django.urls import reverse


class Tenants(models.Model):
    tenant_name = models.CharField('tenant name', max_length=120)

    def __str__(self):
        return self.tenant_name

    def get_absolute_url(self):
        return reverse('tenants.views.TenantDetailView', args=[str(self.pk)])
