# tax_clients/models.py

from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.conf import settings

class TaskTemplate(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class TaxClient(models.Model):
    CONTRACT_STATUS_CHOICES = [
        ('contract', '契約中'),
        ('cancellation', '解約済'),
    ]
    contract_status = models.CharField(
        max_length=100,
        choices=CONTRACT_STATUS_CHOICES,
        blank=True,
        null=True
    )
    number = models.CharField(
        max_length=6,
        blank=True,
        null=True,
        validators=[RegexValidator(r'^\d{1,6}$', '番号は6桁の半角数字で入力してください。')]
    )
    name = models.CharField(max_length=200)
    CORPORATION_TYPE_CHOICES = [
        ('corporate', '法人'),
        ('individual', '個人'),
    ]
    corporation_type = models.CharField(
        max_length=50,
        choices=CORPORATION_TYPE_CHOICES,
        blank=True,
        null=True
    )
    zipcode = models.CharField(
        max_length=8,  # 7桁の数値
        blank=True,
        null=True,
        validators=[RegexValidator(r'^\d{7}$', '郵便番号は7桁の数値で入力してください。')]
    )
    CONSULTING_CONTRACT_CHOICES = [
        ('ongoing', '顧問契約'),
        ('one_time', '単発'),
    ]
    consulting_contract = models.CharField(
        max_length=50,
        choices=CONSULTING_CONTRACT_CHOICES,
        blank=True,
        null=True
    )
    PARTICIPATION_CHOICES = [
        ('contracted', '受託'),
        ('advisory', '顧問先'),
        ('other', 'その他'),
    ]
    participation_accounting = models.CharField(
        max_length=50,
        choices=PARTICIPATION_CHOICES,
        blank=True,
        null=True
    )
    participation_salary = models.CharField(
        max_length=50,
        choices=PARTICIPATION_CHOICES,
        blank=True,
        null=True
    )
    participation_social_insurance = models.CharField(
        max_length=50,
        choices=PARTICIPATION_CHOICES,
        blank=True,
        null=True
    )
    prefecture = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    building = models.CharField(max_length=100, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    email = models.EmailField(blank=True, null=True)
    business_content = models.TextField(blank=True, null=True)
    capital = models.CharField(max_length=50, blank=True, null=True)
    establishment_date = models.DateField(blank=True, null=True)
    etax_no = models.CharField(max_length=50, blank=True, null=True)
    eltax_id = models.CharField(max_length=50, blank=True, null=True)
    nozeiyo_kakunin_bango = models.CharField(max_length=50, blank=True, null=True)
    invoice_no = models.CharField(max_length=50, blank=True, null=True)
    invoice_register_date = models.DateField(blank=True, null=True)
    salary_closing_day = models.CharField(max_length=20, blank=True, null=True)
    salary_payment_month = models.CharField(max_length=20, blank=True, null=True)
    salary_payment_day = models.CharField(max_length=20, blank=True, null=True)
    attendance_soft = models.CharField(max_length=100, blank=True, null=True)
    other_work = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
        
class Task(models.Model):
    client = models.ForeignKey(TaxClient, related_name='tasks', on_delete=models.CASCADE)
    task_template = models.ForeignKey(TaskTemplate, on_delete=models.SET_NULL, null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    creation_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='assigned_tasks', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    approver = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='approved_tasks', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    
    def __str__(self):
        return f"{self.client.name} - {self.task_template.name if self.task_template else 'No Template'}"

class FiscalYear(models.Model):
    client = models.ForeignKey(TaxClient, related_name='fiscal_years', on_delete=models.CASCADE)
    period = models.CharField(max_length=10, null=True, blank=True)  # 期
    closing_date = models.DateField(null=True, blank=True)  # 決算年月日

    def clean(self):
        if not self.period:
            raise ValidationError({'period': '期は必須項目です。'})
        if not self.closing_date:
            raise ValidationError({'closing_date': '決算年月日は必須項目です。'})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        period_str = self.period if self.period else "未設定"
        date_str = self.closing_date.strftime('%Y/%m/%d') if self.closing_date else "未設定"
        return f"{self.client.name} - {period_str} - {date_str}"

class TaxClientDetailView(DetailView):
    model = TaxClient
    template_name = 'tax_clients/tax_client_detail.html'
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fiscal_years'] = self.object.fiscal_years.all()
        return context
