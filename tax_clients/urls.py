# /sphere/tax_clients/urls.py
from django.urls import path
from .views import (
    TaxClientListView, 
    TaxClientCreateView, 
    TaxClientDetailView, 
    TaxClientUpdateView, 
    TaxClientDeleteView, 
    FiscalYearDeleteView,
    FiscalYearUpdateView,
    FiscalYearCreateView,
    BasicInfoUpdateView,
    ContractInfoUpdateView,
    TaxInfoUpdateView,
    FinancialInfoUpdateView
)

urlpatterns = [
    path('', TaxClientListView.as_view(), name='tax_client_list'),
    path('new/', TaxClientCreateView.as_view(), name='tax_client_create'),
    path('<int:pk>/', TaxClientDetailView.as_view(), name='tax_client_detail'),
    path('<int:pk>/update/', TaxClientUpdateView.as_view(), name='tax_client_update'),
    path('<int:pk>/delete/', TaxClientDeleteView.as_view(), name='tax_client_delete'),
    path('<int:client_pk>/fiscal_year/<int:pk>/delete/', FiscalYearDeleteView.as_view(), name='fiscal_year_delete'),
    path('<int:client_pk>/fiscal_year/<int:pk>/update/', FiscalYearUpdateView.as_view(), name='fiscal_year_update'),
    path('<int:client_id>/fiscal_year/new/', FiscalYearCreateView.as_view(), name='fiscal_year_add'),
    path('<int:pk>/update/', BasicInfoUpdateView.as_view(), name='basic_info_update'),
    path('<int:pk>/update/', ContractInfoUpdateView.as_view(), name='contract_info_update'),
    path('<int:pk>/update/', TaxInfoUpdateView.as_view(), name='tax_info_update'),
    path('<int:pk>/update/', FinancialInfoUpdateView.as_view(), name='financial_info_update'),
]
