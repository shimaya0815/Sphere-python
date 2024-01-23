# Generated by Django 4.2.7 on 2024-01-18 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_clients', '0002_taxclient_address_taxclient_attendance_soft_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fiscalyear',
            name='closing_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fiscalyear',
            name='period',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
