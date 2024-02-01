# offices/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import CustomUser, Office
import uuid

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("このメールアドレスは既に使用されています。")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["email"]  # username にメールアドレスを設定

        # 新しい Office インスタンスを作成し、自動生成された UUID を office_id に設定
        office = Office.objects.create(office_id=str(uuid.uuid4()), name='Default Office')
        user.office = office

        if commit:
            user.save()

        return user

class CustomAuthenticationForm(AuthenticationForm):
    office_id = forms.CharField(required=True)

    def clean(self):
        office_id = self.cleaned_data.get('office_id')
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(self.request, username=email, password=password, office_id=office_id)
            if self.user_cache is None or not self.user_cache.office.office_id == office_id:
                raise forms.ValidationError(
                    "メールアドレス、オフィスID、またはパスワードが正しくありません。",
                    code='invalid_login',
                )
        return self.cleaned_data

class UserInviteForm(forms.Form):
    email = forms.EmailField(label='メールアドレス')

class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not CustomUser.objects.filter(email=email).exists():
            raise ValidationError("指定されたメールアドレスは登録されていません。")
        return email
