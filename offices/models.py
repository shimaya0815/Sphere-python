# /sphere/offices/models.py
import random
import string
from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

def generate_office_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

class Office(models.Model):
    office_id = models.CharField(max_length=12, unique=True, default=generate_office_id)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
class CustomUser(AbstractUser):
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
        
class UserInviteForm(forms.Form):
    email = forms.EmailField(label='メールアドレス')
