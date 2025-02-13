from django import forms
from client.models.client_model import ClientModel


class SignUpForm(forms.ModelForm):
    
    """
    Form for ClientModel to sign up.
    
    Fields:
        first_name: Client name.
        last_name: Client last name.
        username: Client username
        password: Client password.
        repeat_password: Client repeated password.
    """

    first_name = forms.CharField(required=True, widget=forms.TextInput())
    last_name = forms.CharField(required=True, widget=forms.TextInput())
    username = forms.CharField(required=True, widget=forms.EmailInput())
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    repeat_password = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = ClientModel
        fields = ["first_name", "last_name", "username", "password", "repeat_password", ]
        

    def __init__(self, *args, **kwargs) -> None:

        """ SignUpForm Initializer. 
        
        Actions:
            - Add Tailwind classes to fields.
        """

        super().__init__(*args, **kwargs)
        tailwind_common_class: str = "p-2 border-b border-b-1 border-primary-earth_tone_4 outline-primary-earth_tone_4"
        tailwind_extra_class: dict[str, str] = {
            "password": "w-full"
        }
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": tailwind_common_class})

            if field_name in tailwind_extra_class:
                field.widget.attrs["class"] += f" {tailwind_extra_class[field_name]}"
                

    def clean(self) -> dict:

        """
        Overwrite `clean` method.
        
        Actions:
            - Set email equal to the username.
        """

        cleaned_data = super().clean()
        username = cleaned_data.get("username")

        if username:
            cleaned_data["email"] = username

        return cleaned_data
    