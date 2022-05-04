
from dataclasses import field
from django import forms
from . import models
from .models import Vulnerability
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)


class CreateAdForm(forms.ModelForm):
    class Meta:
        model = models.Vulnerability
        fields = '__all__'
