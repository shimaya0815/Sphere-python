# Generated by Django 4.2.7 on 2024-01-20 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tax_clients', '0011_remove_taxclient_delivery_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxclient',
            name='mail_magazine',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='new_year_card',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='new_year_card_note',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='office_news',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='seminar_information',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='summer_gift',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='summer_gift_note',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='year_end_gift',
        ),
        migrations.RemoveField(
            model_name='taxclient',
            name='year_end_gift_note',
        ),
    ]