from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _

class CloseAccountForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'password'}))

class ResetAccountForm(forms.Form):
    choices = [
        ('All', 'All'),
        ('5', 'English'),
        ('4', 'French'),
        ('3', 'Italian'),
        ('2', 'Portuguese'),
        ('1', 'Spanish')
    ]
    language = forms.ChoiceField(label='Language', widget=forms.RadioSelect(attrs={'id': 'LanguageRadio'}), choices=choices)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'password'}))

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True, 'placeholder':'old password'}
        ),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder':'password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder':'re-enter password'}),
    )

class ChangeEmailForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'email'}))

class ChangeUsernameForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'username'}))

class ThemesForm(forms.Form):
    choices = [
        ('Light', 'Light'),
        ('Dark', 'Dark'),
    ]
    theme = forms.ChoiceField(widget=forms.RadioSelect(attrs={'id': 'ThemeRadio'}), choices=choices)

class TOTPForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    totp = forms.IntegerField(label='OTP password')