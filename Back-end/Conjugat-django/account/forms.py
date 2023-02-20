from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# classes can go into attrs later when doing design work
class UsernameForm(forms.Form):
    username = forms.CharField(label='Email or Username', widget=forms.TextInput())


class totpForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={}))
    totp = forms.CharField(label='OTP password', widget=forms.TextInput(attrs={}))
    remember_me = forms.BooleanField(label='Remember me', required=False, widget=forms.CheckboxInput())

class passwordForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={}))
    remember_me = forms.BooleanField(label='Remember me', required=False, widget=forms.CheckboxInput())



class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'placeholder':'Email'}),
    )

class SetPasswordForm(SetPasswordForm):
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

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'placeholder':'re-enter password'}))
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Username here',}),
            'email': forms.TextInput(attrs={'placeholder':'Email here',}),
                }
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
        
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data