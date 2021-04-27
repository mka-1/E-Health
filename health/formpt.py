from django import forms
from ClientReg.models import ClientInfo


# creating a form
class ptform(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = ClientInfo

        # specify fields to be used
        fields = [
            "username",
            "email",
            "name",
            "family",
            "password",
            "confirmation",
            "conditions",
            "birth",
            "height",
            "weight"
        ]

