from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control sv-input',
        'placeholder': 'EMAIL'
    }))
    edad = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control sv-input',
        'placeholder': 'EDAD'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'edad']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control sv-input',
            'placeholder': 'YOUR NAME'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control sv-input',
            'placeholder': 'PASSWORD'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control sv-input',
            'placeholder': 'CONFIRMAR PASSWORD'
        })

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            UserProfile.objects.create(
                user=user,
                edad=self.cleaned_data.get('edad')
            )
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control sv-input',
            'placeholder': 'EMAIL'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control sv-input',
            'placeholder': 'PASSWORD'
        })
