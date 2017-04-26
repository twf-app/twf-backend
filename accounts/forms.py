from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Member


class MemberRegistration(UserCreationForm):
    """For CRUDing Users"""

    class Meta(UserCreationForm.Meta):
        model = Member
        fields = UserCreationForm.Meta.fields + ('phone',)
        widgets = {'username': forms.TextInput(attrs={'id': 'user', 'class': 'input'}),
                   'password1': forms.PasswordInput(
                       attrs={'class': 'input', 'type': 'password', 'data-type': 'password'}),
                   'password2': forms.PasswordInput(
                       attrs={'class': 'input', 'type': 'password', 'data-type': 'password'}),
                   'phone': forms.NumberInput(
                       attrs={'id': 'pass', 'class': 'input', 'placeholder': '+1-555-555-5555', 'type': 'tel'}),
                   # 'email': forms.EmailInput(
                   #     attrs={'id': 'pass', 'class': 'input', 'placeholder': 'example@example.com'})
                   }

    def clean(self, *args, **kwargs):
        exists = Member.objects.filter(username=self.cleaned_data['username']).exists()

        if exists:
            raise forms.ValidationError('Username already exists, please enter another username..')
        return super().clean(*args, **kwargs)

#
# class MemberForgotPassword(UserChangeForm):
#     """For CRUDing Users"""
#
#     class Meta(UserChangeForm.Meta):
#         model = Member
#         fields = UserChangeForm.Meta.fields

