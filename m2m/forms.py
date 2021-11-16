from django import forms
from django.forms import ModelForm
from m2m.models import Mail


class MailStartForm(ModelForm):
    recipient = forms.EmailField(label="", min_length=6, max_length=100)

    class Meta:
        model = Mail
        fields = ['recipient']


class MailForm(ModelForm):
    recipient = forms.EmailField(min_length=6, max_length=100)

    class Meta:
        model = Mail
        fields = ['recipient', 'text']
