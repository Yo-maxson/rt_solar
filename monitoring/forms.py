from django import forms
from django.contrib.auth.models import User

from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)


class CreateAdForm(forms.ModelForm):
    class Meta:
        model = models.Vulnerability
        fields = '__all__'
