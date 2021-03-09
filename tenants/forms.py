from django import forms
from django.forms import ModelForm
from tenants.models import Tenants


class TenantCreateForm(forms.Form):
    name = forms.CharField(label='Tenant name', max_length=120, help_text='Your name is initial')
    email = forms.EmailField(help_text='Your email is initial')


# MORE INTUITIVELY realization with model-linked form class - ModelForm
# class TenantCreateForm(ModelForm):
#     class Meta():
#         model = Tenants
#         fields = '__all__'


class TenantUpdateForm(forms.ModelForm):
    class Meta():
        model = Tenants
        fields = '__all__'
