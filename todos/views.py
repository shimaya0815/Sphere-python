#/sphere/todos/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo
from .forms import TodoForm, TodoFilterForm
from django.db.models import ExpressionWrapper, F, DurationField
from datetime import timedelta
from django.utils import timezone
from datetime import timedelta
import datetime

class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        queryset = super().get_queryset()
        form = TodoFilterForm(self.request.GET)
        if form.is_valid():
            if form.cleaned_data['title']:
                queryset = queryset.filter(title__icontains=form.cleaned_data['title'])
            if form.cleaned_data['description']:
                queryset = queryset.filter(description__icontains=form.cleaned_data['description'])
            if form.cleaned_data['status']:
                queryset = queryset.filter(status=form.cleaned_data['status'])
            if form.cleaned_data['recurrence']:
                queryset = queryset.filter(recurrence=form.cleaned_data['recurrence'])
            if form.cleaned_data['assignee']:
                queryset = queryset.filter(assignee__username__icontains=form.cleaned_data['assignee'])
            if form.cleaned_data['approver']:
                queryset = queryset.filter(approver__username__icontains=form.cleaned_data['approver'])
            if form.cleaned_data['client']:
                queryset = queryset.filter(client__name__icontains=form.cleaned_data['client'])
            if form.cleaned_data['fiscal_year']:
                queryset = queryset.filter(fiscal_year=form.cleaned_data['fiscal_year'])
            if form.cleaned_data['category']:
                queryset = queryset.filter(category__icontains=form.cleaned_data['category'])
            if form.cleaned_data['deadline']:
                queryset = queryset.filter(deadline=form.cleaned_data['deadline'])
            if form.cleaned_data['start_time']:
                queryset = queryset.filter(start_time=form.cleaned_data['start_time'])
            if form.cleaned_data['end_time']:
                queryset = queryset.filter(end_time=form.cleaned_data['end_time'])
            if form.cleaned_data['order_by']:
                queryset = queryset.order_by(form.cleaned_data['order_by'])
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = TodoFilterForm(self.request.GET)
        return context

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todos/todo_detail.html'

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        office_id = self.request.user.office.office_id
        return reverse_lazy('todo_list', kwargs={'office_id': office_id})

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_form.html'

    def get_success_url(self):
        office_id = self.request.user.office.office_id
        return reverse_lazy('todo_list', kwargs={'office_id': office_id})

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todos/todo_confirm_delete.html'

    def get_success_url(self):
        office_id = self.request.user.office.office_id
        return reverse_lazy('todo_list', kwargs={'office_id': office_id})


class TimeSheetView(LoginRequiredMixin, TemplateView):
    template_name = 'todos/timesheet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_tasks = Todo.objects.filter(user=self.request.user).annotate(
            duration=ExpressionWrapper(
                F('end_time') - F('start_time'),
                output_field=DurationField()
            )
        )
        context['user_tasks'] = user_tasks
        context['total_time'] = sum(task.duration for task in user_tasks if task.duration)
        return context

class TimeSheetView(LoginRequiredMixin, TemplateView):
    template_name = 'todos/timesheet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_tasks = Todo.objects.filter(user=self.request.user).annotate(
            duration=ExpressionWrapper(
                F('end_time') - F('start_time'),
                output_field=DurationField()
            )
        )
        context['user_tasks'] = user_tasks
        total_time = timedelta()
        for task in user_tasks:
            if task.duration:
                total_time += task.duration
        context['total_time'] = total_time
        return context

class TimeSheetView(LoginRequiredMixin, TemplateView):
    template_name = 'todos/timesheet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        week_ago = today - timedelta(days=6)

        # 当日のタスクと作業時間
        today_tasks = Todo.objects.filter(
            user=self.request.user,
            start_time__date=today
        ).annotate(duration=ExpressionWrapper(F('end_time') - F('start_time'), output_field=DurationField()))
        today_total = sum((task.duration for task in today_tasks if task.duration), timedelta())

        # 過去7日間のタスク
        week_tasks = Todo.objects.filter(
            user=self.request.user,
            start_time__date__gte=week_ago,
            start_time__date__lte=today
        ).annotate(duration=ExpressionWrapper(F('end_time') - F('start_time'), output_field=DurationField()))

        # 週単位の作業時間の集計
        week_total = sum((task.duration for task in week_tasks if task.duration), timedelta())

        context['today_tasks'] = today_tasks
        context['today_total'] = today_total
        context['week_total'] = week_total
        return context
