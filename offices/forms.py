# offices/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import CustomUser, Office
import uuid


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]

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
            if self.user_cache is None or self.user_cache.office.office_id != office_id:
                raise forms.ValidationError(
                    "メールアドレス、オフィスID、またはパスワードが正しくありません。",
                    code='invalid_login',
                )
        return self.cleaned_data
        
class UserInviteForm(forms.Form):
    email = forms.EmailField(label='メールアドレス')
        
        