from django.forms.models import ModelForm
from payments.models import Payments


class PaymentCreationForm(ModelForm):
    class Meta():
        model = Payments
        fields = '__all__'