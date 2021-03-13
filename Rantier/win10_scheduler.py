import os
import sys
import django
from datetime import datetime, timedelta


# necessary requirements to run script for Django
sys.path.append('C:\\Users\home_\PycharmProjects\Rantier')  # add <path_to_script> to system path for corrett modules import.
os.environ['DJANGO_SETTINGS_MODULE'] = 'Rantier.settings'  # set Django-needed settings module
django.setup()

from payments.models import Payments
from contracts.models import Contracts

# def payment_create():
#     contract = Contracts.objects.get(pk=1)
#     payment = Payments.objects.create(
#         contract=contract,
#         description='CRON',
#         rent_payment=1984,
#     )
#     return payment

# Т.к. скрипт использует аналог crоn для win10 (Task Scheduler) и флага "auto_now_add=True" в поле
# created_at - создание нового объекта Payments И значение этого поля будет генерироваться в момент
# запуска данного скрипта.
# Чтобы "разорвать" момент запуска скрипта и генерации значения поля created_at необходимо
# отменить флаг "auto_now_add=True". Например:

def payment_create():
    """
    Auto create 'payments for all contracts with date step = 30 days from last payment (till contract start date)'
    :return:
    """
    contracts = Contracts.objects.all()
    for contract in contracts:
        payment = Payments.objects.create(
            contract=contract,
            description='auto genereted check',
            created_at=Payments.objects.order_by('-created_at')[0].created_at + timedelta(30),  # Автоматическое создание счета раз в 30 дней с даты заключения контракта. Рассчет производится на основании предыдущего объекта модели
            rent_payment=contract.cost
        )
    return payment

if __name__ == '__main__':
    payment_create()
