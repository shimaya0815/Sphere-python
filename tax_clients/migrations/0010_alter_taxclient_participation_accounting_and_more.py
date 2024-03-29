# Generated by Django 4.2.7 on 2024-01-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_clients', '0009_taxclient_consulting_contract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxclient',
            name='participation_accounting',
            field=models.CharField(blank=True, choices=[('contracted', '受託'), ('advisory', '顧問先'), ('other', 'その他')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='taxclient',
            name='participation_salary',
            field=models.CharField(blank=True, choices=[('contracted', '受託'), ('advisory', '顧問先'), ('other', 'その他')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='taxclient',
            name='participation_social_insurance',
            field=models.CharField(blank=True, choices=[('contracted', '受託'), ('advisory', '顧問先'), ('other', 'その他')], max_length=50, null=True),
        ),
    ]
