# Generated by Django 4.2.7 on 2024-01-17 11:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxclient',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='attendance_soft',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='building',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='business_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='capital',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='consumption_tax',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='corporation_tax',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='corporation_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='delivery_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='delivery_building',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='delivery_city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='delivery_prefecture',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='delivery_same',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='delivery_zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='depreciable_property_tax',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='eltax_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='establishment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='etax_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='interview_frequency',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='invoice_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='invoice_register_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='local_tax_method',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='mail_magazine',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='national_tax_method',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='new_year_card',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='new_year_card_note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='nozeiyo_kakunin_bango',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='office_news',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='other_work',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='participation_accounting',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='participation_period',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='participation_salary',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='participation_social_insurance',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='prefecture',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='resident_tax_method',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='salary_closing_day',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='salary_payment_day',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='salary_payment_month',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='seminar_information',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='statutory_report',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='summer_gift',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='summer_gift_note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='tel',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='trial_balance_frequency',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='withholding_income_tax1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='withholding_income_tax2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='withholding_method',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='withholding_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='year_end_adjustment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='year_end_gift',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='year_end_gift_note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taxclient',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
