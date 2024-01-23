#/sphere/todos/models.py
from django.db import models
from django.conf import settings
from django.db.models import ExpressionWrapper, F, Sum, DurationField
from tax_clients.models import TaxClient, FiscalYear  # TaxClient と FiscalYear のインポート

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    STATUS_CHOICES = [
        ('未着手', '未着手'),
        ('仕掛中', '仕掛中'),
        ('実施者完了', '実施者完了'),
        ('レビュー中', 'レビュー中'),
        ('承認済', '承認済'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='未着手')
    RECURRENCE_CHOICES = [
        ('', '-----'),
        ('daily', '毎日'),
        ('weekly', '毎週'),
        ('monthly', '毎月'),
        ('yearly', '毎年'),
    ]
    recurrence = models.CharField(max_length=10, choices=RECURRENCE_CHOICES, default='', blank=True)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='assigned_todos', on_delete=models.SET_NULL, null=True, blank=True)
    approver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='approved_todos', on_delete=models.SET_NULL, null=True, blank=True)
    
    client = models.ForeignKey(TaxClient, on_delete=models.SET_NULL, null=True, blank=True)
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ユーザー
    
    
    def __str__(self):
        return self.title

    @classmethod
    def total_time(cls, user):
        """
        指定されたユーザーのTodoの合計時間を返します。
        """
        total_duration = cls.objects.filter(user=user).annotate(
            duration=ExpressionWrapper(
                F('end_time') - F('start_time'),
                output_field=DurationField()
            )
        ).aggregate(total=Sum('duration'))

        return total_duration['total']
