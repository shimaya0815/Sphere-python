# tax_clients/forms.py
from django import forms
from .models import TaxClient, FiscalYear, Task

class TaxClientForm(forms.ModelForm):
    class Meta:
        model = TaxClient
        fields = [
            'contract_status', 'number', 'name', 'corporation_type', 'consulting_contract', 'participation_accounting', 'participation_salary', 
            'participation_social_insurance', 'zipcode', 'prefecture', 'city', 'address', 'building', 'tel', 
            'email', 'business_content', 'capital', 'establishment_date', 
            'etax_no', 'eltax_id', 'nozeiyo_kakunin_bango', 'invoice_no', 'invoice_register_date', 'salary_closing_day', 'salary_payment_month', 
            'salary_payment_day', 'attendance_soft', 'other_work',
        ]
        labels = {
            'contract_status': '契約状況',
            'number': 'クライアントNo',
            'name': '名前',
            'corporation_type': '法人・個人区分',
            'consulting_contract': '顧問契約',
            'participation_accounting': '関与形式 経理',
            'participation_salary': '関与形式 給与',
            'participation_social_insurance': '関与形式 社保',
            'zipcode': '郵便番号',
            'prefecture': '都道府県',
            'city': '市区町村',
            'address': '以下住所',
            'building': '建物名',
            'tel': '電話番号',
            'email': 'Eメール',
            'business_content': '事業内容',
            'capital': '資本金',
            'establishment_date': '設立日/開業日',
            'etax_no': 'e-Tax 利用者識別番号',
            'eltax_id': 'eLTAX 利用者ID',
            'nozeiyo_kakunin_bango': '納税用確認番号',
            'invoice_no': 'インボイス登録番号',
            'invoice_register_date': 'インボイス登録日',
            'salary_closing_day': '給与締日',
            'salary_payment_month': '給与支払月',
            'salary_payment_day': '給与支払日',
            'attendance_soft': '勤怠ソフト',
            'other_work': 'その他の受託作業',
        }

class FiscalYearForm(forms.ModelForm):
    class Meta:
        model = FiscalYear
        fields = ['period', 'closing_date']
        widgets = {
            'closing_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
        
class BasicInfoForm(forms.ModelForm):
    class Meta:
        model = TaxClient
        fields = [
            'number', 'name', 'corporation_type', 'zipcode', 'prefecture', 'city', 
            'address', 'building', 'tel', 'email', 'capital', 'establishment_date'
        ]

class ContractInfoForm(forms.ModelForm):
    class Meta:
        model = TaxClient
        fields = [
            'contract_status', 'consulting_contract', 'participation_accounting', 
            'participation_salary', 'participation_social_insurance', 'other_work'
        ]

class TaxInfoForm(forms.ModelForm):
    class Meta:
        model = TaxClient
        fields = [
            'etax_no', 'eltax_id', 'nozeiyo_kakunin_bango', 'invoice_no', 'invoice_register_date'
        ]

class FinancialInfoForm(forms.ModelForm):
    class Meta:
        model = TaxClient
        fields = [
            'salary_closing_day', 'salary_payment_month', 'salary_payment_day', 'attendance_soft'
        ]

class FiscalYearForm(forms.ModelForm):
    class Meta:
        model = FiscalYear
        fields = ['period', 'closing_date']
        widgets = {
            'closing_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_template', 'is_completed', 'creation_date', 'due_date', 'assignee', 'approver']
        widgets = {
            'creation_date': forms.DateInput(attrs={'type': 'date'}),
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }
