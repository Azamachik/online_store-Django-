from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm
import re


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'type': "text", 'required': True}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'type': "password", 'required': True}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'passoword', )


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'type': "text", 'required': True}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'type': "password", 'required': True}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'type': "password", 'required': True}))
    usable_password = None

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        label = {'username': 'Логин',
                 'first_name': 'Имя',
                 'last_name': 'Фамилия',
                 }
        widgets = {
            'email': forms.TextInput(attrs={'type': "text", 'required': True}),
            'first_name': forms.TextInput(attrs={'type': "text", 'required': True}),
            'last_name': forms.TextInput(attrs={'type': "text", 'required': True}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        pattern = r'[A-Za-z0-9_-]{4,}@[A-Za-z]{1,}.[A-Za-z]{1,}'
        if re.fullmatch(pattern, email):
            if get_user_model().objects.filter(email=email).exists():
                raise forms.ValidationError('Пользователь с таким e-mail уже зарегистрирован')
        else:
            raise forms.ValidationError('Некорректный e-mail адрес')

        return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин')
    email = forms.CharField(disabled=True, label='Адрес электронной почты')

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name',)
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }


class PasswordChangeUserForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'type': "text", 'required': True}))
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'type': "password", 'required': True}))
    new_password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'type': "password", 'required': True}))

    class Meta:
        model = get_user_model()
        fields = ('old_password', 'new_password1', 'new_password2', )
