from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator, EmailValidator

from todo_app.validators import validate_name, password_validator


class TodoForm(forms.Form):
    title = forms.CharField(label='title', max_length=20)
    description = forms.CharField(widget=forms.Textarea)


class FormName(forms.Form):
    name = forms.CharField(validators=[validate_name, MinLengthValidator(6)])
    age = forms.IntegerField(widget=forms.NumberInput,
                             validators=[MinValueValidator(0, message='The age cannot be less than zero.')])
    email = forms.EmailField(widget=forms.EmailInput, validators=[EmailValidator(message='Enter a valid email.')])
    password = forms.CharField(widget=forms.PasswordInput,
                               validators=[MinLengthValidator(8, message='Enter a valid password.'),
                                           password_validator])
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput, max_length=0, validators=[])

    def clean_bot_catcher(self):
        bot_catcher = ''
        if len(bot_catcher) > 0:
            raise forms.ValidationError('GOTCHA BOT!')
        return bot_catcher
