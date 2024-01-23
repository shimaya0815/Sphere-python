# Generated by Django 4.2.7 on 2024-01-20 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tax_clients', '0013_remove_taxclient_local_tax_method_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxclient',
            name='consumption_tax',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='corporation_tax',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='depreciable_property_tax',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='interview_frequency',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='participation_period',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='statutory_report',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='trial_balance_frequency',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='withholding_income_tax1',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='withholding_income_tax2',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='withholding_time',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='year_end_adjustment',
        ),
    ]