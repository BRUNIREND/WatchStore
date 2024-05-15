from .models import RegisteredUsers
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(ModelForm):
    """
    Переопределенная форма регистрации пользователя
    """
    class Meta:
        model = RegisteredUsers
        # fields = UserCreationForm.Meta.fields + ('name', 'surname', 'email', 'password', 'password_check')
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
    # def clean_email(self):
    #     """
    #     проверка email на уникальность
    #     """
    #     email = self.cleaned_data.get('email')
    #     if email and RegisteredUsers.objects.filter(email=email).exists():
    #         raise
    #     return email