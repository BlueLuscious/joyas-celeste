from back.models.client_model import ClientModel
from django import forms


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput())
    last_name = forms.CharField(required=True, widget=forms.TextInput())
    username = forms.CharField(required=True, widget=forms.EmailInput())
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    repeat_password = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = ClientModel
        fields = ["first_name", "last_name", "username", "password", "repeat_password", ]
        

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        tailwind_common_class = "p-2 border-b border-b-1 border-primary-earth_tone_4 outline-primary-earth_tone_4"
        tailwind_extra_class = {
            "password": "w-full"
        }
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": tailwind_common_class})

            if field_name in tailwind_extra_class:
                field.widget.attrs["class"] += f" {tailwind_extra_class[field_name]}"
                