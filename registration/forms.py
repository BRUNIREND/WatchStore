from .models import User
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, CharField, PasswordInput, ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserChangeForm


class UserLoginForm(AuthenticationForm):
    username = CharField()
    password = CharField()

    # username = CharField(label='Имя',
    #     widget=TextInput(attrs={"autofocus": True,
    #                             'class': 'form-control',
    #                             'placeholder': 'Введите ваше имя пользователя'})
    # )
    # password = CharField(
    #     label='Пароль',
    #     widget=PasswordInput(attrs={"autocomplete": "current-password",
    #                             'class': 'form-control',
    #                             'placeholder': 'Введите ваш пароль'})
    # )
    class Meta:
        model = User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = {
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        }

    first_name = CharField(required=False)
    last_name = CharField()
    username = CharField()
    email = CharField()
    password1 = CharField()
    password2 = CharField()


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
        )

    image = ImageField()
    first_name = CharField()
    last_name = CharField()
    username = CharField()
    email = CharField()
# class RegistrationForm(ModelForm):
#     """
#     Переопределенная форма регистрации пользователя
#     """
#     class Meta:
#         # model = RegisteredUsers
#         # fields = UserCreationForm.Meta.fields + ('name', 'surname', 'email', 'password', 'password_check')
#         fields = {'name', 'surname', 'email', 'password', 'password_check'}
#
#         widgets = {
#             'name': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Имя'
#             }),
#             'surname': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Фамилия'
#             }),
#             'email': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Электронная почта'
#
#             }),
#             'password': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Пароль'
#             }),
#             'password_check': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Повторите пароль'
#             }),
#         }
# def clean_email(self):
#     """
#     проверка email на уникальность
#     """
#     email = self.cleaned_data.get('email')
#     if email and RegisteredUsers.objects.filter(email=email).exists():
#         raise
#     return email
