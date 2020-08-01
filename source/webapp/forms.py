from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]


class BookForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Имя',
                            widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    author = forms.CharField(max_length=40, required=True, label='Email',
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    text = forms.CharField(max_length=3000, required=True, label="Текст",
                           widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Статус',
                               initial=default_status)
