from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, EmailValidator


class TodoForm(forms.Form):
    title = forms.CharField(label='title', max_length=20)
    description = forms.CharField(widget=forms.Textarea)


class FormName(forms.Form):
    name = forms.CharField(validators=[MinLengthValidator(6)])
    age = forms.IntegerField(widget=forms.NumberInput,
                             validators=[MinValueValidator(0, message='The age cannot be less than zero.')])
    email = forms.EmailField(widget=forms.EmailInput, validators=[EmailValidator(message='Enter a valid email.')])
    password = forms.CharField(widget=forms.PasswordInput,
                               validators=[MinLengthValidator(8, message='Enter a valid password.')
                                           ])
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput, max_length=0, validators=[])

    def clean_bot_catcher(self):
        bot_catcher = ''
        if len(bot_catcher) > 0:
            raise ValidationError('GOTCHA BOT!')
        return bot_catcher

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name[0].isupper():
            raise ValidationError('The name must start with an uppercase letter.')
        return name

# def validate_name(name):
#     if not name[0].isupper():
#         raise forms.ValidationError('The name must start with an uppercase letter.')
#
#
# def password_validator(password):
#     for char in password:
#         if not char.isdigit() or not char.isalpha():
#             raise forms.ValidationError(f'Enter a valid password.')
