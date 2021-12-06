from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from .models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите e-mail',
        required=True,
        widget=forms.TextInput(attrs={'class': 'registration_form_field', 'placeholder': 'Введите e-mail*'}),
    )
    username = forms.CharField(
        label='Введите логин',
        required=True,
        widget=forms.TextInput(attrs={'class': 'registration_form_field', 'placeholder': 'Введите логин*'}),
    )

    first_name = forms.CharField(
        label='Имя',
        required=False,
        widget=forms.TextInput(attrs={'class': 'registration_form_field', 'placeholder': 'Введите имя'}),
    )

    last_name = forms.CharField(
        label='Фамилия',
        required=False,
        widget=forms.TextInput(attrs={'class': 'registration_form_field', 'placeholder': 'Введите фамилию'}),
    )

    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        help_text='Пароль должен состоять не менее чем из 8 знаков, содержать цифры и символы в верхнем и нижнем регистрах',
        widget=forms.PasswordInput(attrs={'class': 'registration_form_field', 'placeholder': 'Введите пароль*'}),
    )

    password2 = forms.CharField(
        label='Введите пароль ещё раз',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'registration_form_field', 'placeholder': 'Повторите пароль*'}),
    )

    # choicefield = forms.ModelChoiceField(queryset=User.objects.all()) - поле с выбором значений из какой-либо таблицы

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]


class UpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(attrs={'class': 'update_user_form_field', 'placeholder': 'Введите e-mail*'}),
    )

    username = forms.CharField(
        label='Логин',
        required=True,
        widget=forms.TextInput(attrs={'class': 'update_user_form_field', 'placeholder': 'Введите логин*'}),
    )

    first_name = forms.CharField(
        label='Имя',
        required=False,
        widget=forms.TextInput(attrs={'class': 'update_user_form_field', 'placeholder': 'Введите имя'}),
    )

    last_name = forms.CharField(
        label='Фамилия',
        required=False,
        widget=forms.TextInput(attrs={'class': 'update_user_form_field', 'placeholder': 'Введите фамилию'}),
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
        ]


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузить фото',
        required=False,
        widget=forms.FileInput,
    )

    class Meta:
        model = Profile
        fields = ['img']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'login_form_field', 'placeholder': 'Логин'})
        self.fields['username'].label = 'Введите логин'
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'login_form_field', 'placeholder': 'Пароль'})
        self.fields['password'].label = 'Введите пароль'


class EditPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Введите старый пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'change_password_form_field', 'placeholder': 'Старый пароль*'}),
    )

    new_password1 = forms.CharField(
        label='Введите новый пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'change_password_form_field', 'placeholder': 'Новый пароль*'}),
    )

    new_password2 = forms.CharField(
        label='Подтверждение нового пароля',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'change_password_form_field', 'placeholder': 'Повторите новый пароль*'}),
    )

    class Meta:
        model = User
        fields = [
            'old_password',
            'new_password1',
            'new_password2',
        ]