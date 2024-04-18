from .models import RegisteredUsers
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class RegistrationForm(ModelForm):
    class Meta:
        model = RegisteredUsers
        fields = {'name', 'surname', 'email', 'password', 'password_check'}

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'surname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Электронная почта'

            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
            'password_check': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль'
            }),
        }