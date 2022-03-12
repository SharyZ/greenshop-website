from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailInput, ModelForm, PasswordInput, TextInput, CharField

from .models import Customer

INPUT_CLASSES = 'focus:border-primary-500 focus:ring-primary-300 block w-full rounded-md border-gray-100 shadow-sm focus:ring-2'


class CustomerSignupForm(UserCreationForm):
    password1 = CharField(
        widget=PasswordInput(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Password',
        })
    )
    password2 = CharField(
        widget=PasswordInput(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Password confirmation',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email',)
        widgets = {
            'username': TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Username',
            }),
            'email': EmailInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'E-mail',
            }),
        }


class CustomerProfileEditForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
