# Generated by Django 4.2.7 on 2024-01-20 08:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_clients', '0005_taxclient_contract_status_alter_taxclient_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxclient',
            name='contract_status',
            field=models.CharField(blank=True, choices=[('contract', '契約中'), ('cancellation', '解約済')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='taxclient',
            name='zipcode',
            field=models.CharField(blank=True, max_length=8, null=True, validators=[django.core.validators.RegexValidator('^\\d{7}$', '郵便番号は7桁の数値で入力してください。')]),
        ),
    ]
