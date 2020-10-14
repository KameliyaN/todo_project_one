from django import forms


class TodoForm(forms.Form):
    title = forms.CharField(label='title', max_length=20)
    description = forms.CharField(widget=forms.Textarea)


class FormName(forms.Form):
    name=forms.CharField(validators=[])