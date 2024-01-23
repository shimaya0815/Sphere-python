# /sphere/tax_clients/views.py
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from .models import TaxClient, FiscalYear, Task, TaskTemplate
from django.http import JsonResponse
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from .forms import (TaxClientForm, FiscalYearForm, TaskForm,
                    BasicInfoForm, ContractInfoForm, TaxInfoForm, FinancialInfoForm)

User = get_user_model()

def get_office_id(request):
    if request.user.is_authenticated and hasattr(request.user, 'office'):
        return request.user.office.office_id
    return None

class TaxClientListView(ListView):
    model = TaxClient
    template_name = 'tax_clients/tax_client_list.html'
    context_object_name = 'tax_clients'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['office_id'] = get_office_id(self.request)
        return context

class TaxClientCreateView(CreateView):
    model = TaxClient
    form_class = TaxClientForm
    template_name = 'tax_clients/tax_client_form.html'

    def get_success_url(self):
        office_id = get_office_id(self.request)
        return reverse('tax_client_list', kwargs={'office_id': office_id})

class TaxClientDetailView(DetailView):
    model = TaxClient
    template_name = 'tax_clients/tax_client_detail.html'
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['office_id'] = get_office_id(self.request)
        context['fiscal_years'] = self.object.fiscal_years.all()
        context['tasks'] = self.object.tasks.all()
        return context
        
class TaxClientUpdateView(UpdateView):
    model = TaxClient
    form_class = TaxClientForm
    template_name = 'tax_clients/tax_client_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['office_id'] = get_office_id(self.request)
        context['client'] = self.object
        context['basic_info_form'] = BasicInfoForm(instance=self.object)
        context['contract_info_form'] = ContractInfoForm(instance=self.object)
        context['tax_info_form'] = TaxInfoForm(instance=self.object)
        context['financial_info_form'] = FinancialInfoForm
        context['fiscal_years'] = FiscalYear.objects.filter(client=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        basic_info_form = BasicInfoForm(request.POST, instance=self.object)
        contract_info_form = ContractInfoForm(request.POST, instance=self.object)
        tax_info_form = TaxInfoForm(request.POST, instance=self.object)
        financial_info_form = FinancialInfoForm(request.POST, instance=self.object)

        if form.is_valid() and basic_info_form.is_valid() and contract_info_form.is_valid() and tax_info_form.is_valid() and financial_info_form.is_valid():
            return self.form_valid(form, basic_info_form, contract_info_form, tax_info_form, financial_info_form)
        else:
            return self.form_invalid(form, basic_info_form, contract_info_form, tax_info_form, financial_info_form)

    def form_valid(self, form, basic_info_form, contract_info_form, tax_info_form, financial_info_form):
        form.save()
        basic_info_form.save()
        contract_info_form.save()
        tax_info_form.save()
        financial_info_form.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form, basic_info_form, contract_info_form, tax_info_form, financial_info_form):
        return self.render_to_response(
            self.get_context_data(form=form, 
                                  basic_info_form=basic_info_form, 
                                  contract_info_form=contract_info_form, 
                                  tax_info_form=tax_info_form,
                                  financial_info_form=financial_info_form))

    def get_success_url(self):
        office_id = get_office_id(self.request)
        return reverse('tax_client_detail', kwargs={'office_id': office_id, 'pk': self.object.pk})
            
class TaxClientDeleteView(DeleteView):
    model = TaxClient
    template_name = 'tax_clients/tax_client_confirm_delete.html'

    def get_success_url(self):
        office_id = get_office_id(self.request)
        return reverse('tax_client_list', kwargs={'office_id': office_id}) if office_id else reverse('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['office_id'] = get_office_id(self.request)
        context['fiscal_years'] = self.object.fiscal_years.all()
        return context

class FiscalYearDeleteView(DeleteView):
    model = FiscalYear
    template_name = 'tax_clients/fiscal_year_confirm_delete.html'
    context_object_name = 'object'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.client_id = self.object.client.id
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        office_id = get_office_id(self.request)
        return reverse('tax_client_update', kwargs={'office_id': office_id, 'pk': self.client_id}) if office_id else reverse('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['office_id'] = get_office_id(self.request)
        return context

class FiscalYearUpdateView(UpdateView):
    model = FiscalYear
    form_class = FiscalYearForm
    template_name = 'tax_clients/fiscal_year_form.html'

    def get_success_url(self):
        office_id = get_office_id(self.request)
        return reverse('tax_client_detail', kwargs={'office_id': office_id, 'pk': self.object.client.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['office_id'] = get_office_id(self.request)
        return context
        
class FiscalYearCreateView(CreateView):
    model = FiscalYear
    form_class = FiscalYearForm
    template_name = 'tax_clients/fiscal_year_form.html'

    def form_valid(self, form):
        form.instance.client_id = self.kwargs['client_id']
        return super().form_valid(form)

    def get_success_url(self):
        # 決算期追加後のリダイレクト先（例：クライアント詳細ページ）
        return reverse('tax_client_detail', kwargs={'office_id': self.request.user.office.office_id, 'pk': self.kwargs['client_id']})
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['office_id'] = self.request.user.office.office_id
        return context
        
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tax_clients/task_form.html'

    def form_valid(self, form):
        form.instance.client_id = self.kwargs['client_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tax_client_detail', kwargs={'office_id': self.request.user.office.office_id, 'pk': self.kwargs['client_id']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['office_id'] = self.request.user.office.office_id
        return context
        
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tax_clients/task_form.html'

    def get_success_url(self):
        return reverse('tax_client_detail', kwargs={'office_id': self.request.user.office.office_id, 'pk': self.object.client.id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['office_id'] = self.request.user.office.office_id
        return context
        
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tax_clients/task_confirm_delete.html'

    def get_success_url(self):
        return reverse('tax_client_detail', kwargs={'office_id': self.request.user.office.office_id, 'pk': self.object.client.id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['office_id'] = self.request.user.office.office_id
        return context

class BasicInfoUpdateView(UpdateView):
    model = TaxClient
    form_class = BasicInfoForm
    template_name = 'tax_clients/tax_client_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['office_id'] = get_office_id(self.request)
        context['client'] = self.object
        return context

    def get_success_url(self):
        office_id = get_office_id(self.request)
        return reverse('tax_client_detail', kwargs={'office_id': office_id, 'pk': self.object.pk})

class ContractInfoUpdateView(UpdateView):
    model = TaxClient
    form_class = ContractInfoForm
    template_name = 'tax_clients/tax_client_form.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, '契約情報が更新されました。')
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('tax_client_detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['office_id'] = self.request.user.office.office_id
        return context

class TaxInfoUpdateView(UpdateView):
    model = TaxClient
    form_class = TaxInfoForm
    template_name = 'tax_clients/tax_client_form.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, '税務情報が更新されました。')
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('tax_client_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['office_id'] = self.request.user.office.office_id
        return context

class FinancialInfoUpdateView(UpdateView):
    model = TaxClient
    form_class = FinancialInfoForm
    template_name = 'tax_clients/tax_client_form.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, '給与情報が更新されました。')
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('tax_client_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['office_id'] = self.request.user.office.office_id
        return context