# Generated by Django 3.1.7 on 2021-03-08 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenants', '0001_initial'),
        ('apartments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contracts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concluded_at', models.DateField(auto_now_add=True)),
                ('expiration_date', models.DateField()),
                ('cost', models.IntegerField()),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartment', to='apartments.apartments')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenants.tenants', verbose_name='tenant name')),
            ],
        ),
    ]
