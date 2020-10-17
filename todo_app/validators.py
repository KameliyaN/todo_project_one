

from django import forms


def validate_name(name):
    if not name[0].isupper():
        raise forms.ValidationError('The name must start with an uppercase letter.')


def password_validator(password):
    for char in password:
        if not char.isdigit() or not char.isalpha():
            raise forms.ValidationError(f'Enter a valid password.')
# pattern = r'([a-z]+)|([A-Z]+)|([0-9]+)'
# matches = re.findall(pattern, password)
