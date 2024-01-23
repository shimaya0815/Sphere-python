# offices/views.py
from django.views.generic import CreateView, TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser, Office
from .forms import CustomUserCreationForm, UserInviteForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        office = Office.objects.create(name=user.username)  # 事業所を自動生成
        user.office = office
        user.save()
        login(self.request, user)
        messages.success(self.request, f'事業所ID {office.office_id} が発行されました。')
        return redirect('dashboard', office_id=office.office_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DashboardView(TemplateView):
    template_name = 'offices/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CustomLoginView(DefaultLoginView):
    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            return f'/{user.office.office_id}/dashboard/'
        return super().get_success_url()


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'offices/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return CustomUser.objects.filter(office=self.request.user.office)


class UserInviteView(FormView):
    template_name = 'offices/user_invite.html'
    form_class = UserInviteForm
    success_url = reverse_lazy('user_invite')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        # ここで実際の招待処理を実装します（例：招待メールの送信）
        # メール送信の詳細はプロジェクトの設定に応じて調整してください
        send_mail(
            'アプリケーションへの招待',
            'アプリケーションに参加するためのリンク: http://yourapp.com/',
            'from@example.com',
            [email],
            fail_silently=False,
        )
        messages.success(self.request, f'{email} に招待メールを送信しました。')
        return super().form_valid(form)