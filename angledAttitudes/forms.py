__author__ = 'davidaxelrod'

from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


class UserForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=3, help_text="Enter a username")
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(_("This username has already existed."))

    def clean(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        email = self.cleaned_data.get('email')
        try:
            email_taken = User.objects.get(email__iexact=email)
            if email_taken:
                raise forms.ValidationError(_("A user already has that email address"))
        except User.DoesNotExist:
            pass

        if password1 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return self.cleaned_data
