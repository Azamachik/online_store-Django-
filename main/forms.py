from captcha.fields import CaptchaField
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=30,
                           widget=forms.TextInput(attrs={'type': 'text', 'class': 'input'}))
    email = forms.EmailField(label='Адрес электронной почты',
                             widget=forms.TextInput(attrs={'type': 'email', 'class': 'input'}))
    ##phone = forms.
    content = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'input'}))
    captcha = CaptchaField(label='Введите слово с картинки')
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['name'].initial = user.username
            self.fields['name'].widget.attrs['readonly'] = True
            self.fields['email'].initial = user.email
            #self.fields['email'].widget.attrs['readonly'] = True


