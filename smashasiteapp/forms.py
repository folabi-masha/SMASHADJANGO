from django import forms

class NameForm(forms.Form):
    email = forms.CharField(label='email', max_length=100)