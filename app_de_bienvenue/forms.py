from django import forms

class FormContact(forms.Form):
    nom = forms.CharField(max_length=100)
    email = forms.CharField(max_length=50)
    message = forms.CharField(max_length=200)