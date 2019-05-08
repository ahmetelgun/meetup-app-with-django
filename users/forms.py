from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, CustomUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    # -*- coding: utf-8 -*-
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False
    )
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'about')
      
    def save(self, commit=True):
        user = super().save(commit=False)
        
        #create username with use first_name and last_name
        username_temp = self.cleaned_data["first_name"]+ self.cleaned_data["last_name"]
        user.username = CustomUserManager.create_username(username_temp)

        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
