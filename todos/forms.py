# todos/forms.py
from django import forms
from .models import Todo
from django.forms.widgets import DateTimeInput

class TodoForm(forms.ModelForm):
    # 再発生のためのカスタム選択肢
    RECURRENCE_CHOICES = [
        ('', '-----'),
        ('daily', '毎日'),
        ('weekly', '毎週'),
        ('monthly', '毎月'),
        ('yearly', '毎年'),
    ]
    
    # 再発生フィールドの追加
    recurrence = forms.ChoiceField(choices=RECURRENCE_CHOICES, required=False)

    class Meta:
        model = Todo
        fields = ['title', 'description', 'status', 'recurrence', 'assignee', 'approver', 'client', 'fiscal_year', 'category', 'deadline', 'start_time', 'end_time']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'start_time': DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time:
            if end_time < start_time:
                raise forms.ValidationError("終了時間は開始時間よりも後でなければなりません。")

        return cleaned_data

class TodoFilterForm(forms.Form):
    title = forms.CharField(required=False)
    description = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[('', ''), ('pending', 'Pending'), ('completed', 'Completed')], required=False)
    recurrence = forms.ChoiceField(choices=[('', ''), ('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], required=False)
    assignee = forms.CharField(required=False)
    approver = forms.CharField(required=False)
    client = forms.CharField(required=False)
    fiscal_year = forms.CharField(required=False)
    category = forms.CharField(required=False)
    deadline = forms.DateField(required=False)
    start_time = forms.DateTimeField(required=False)
    end_time = forms.DateTimeField(required=False)
    order_by = forms.ChoiceField(choices=[('title', 'Title'), ('deadline', 'Deadline')], required=False)
    
    