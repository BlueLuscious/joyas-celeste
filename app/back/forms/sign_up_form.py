from django import forms
from back.models.client_model import ClientModel

class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "input", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "input", "placeholder": "Last Name"}))
    username = forms.CharField(widget=forms.EmailInput(attrs={"class": "input", "placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "Password"}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "Repeat Password"}))

    class Meta:
        model = ClientModel
        fields = ["first_name", "last_name", "username", "password", "repeat_password", ]
        