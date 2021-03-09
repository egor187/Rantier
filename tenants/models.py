from django.db import models
from django.urls import reverse


class Tenants(models.Model):
    name = models.CharField('tenant name', max_length=120)
    email = models.EmailField()



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tenants:tenant_detail', args=[self.pk])
