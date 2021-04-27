from django import forms
from .models import ConfirmedAppointment


# creating a form
class Apptformr(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = ConfirmedAppointment

        # specify fields to be used
        fields = [
            "time",
            "name",
            "username",
            "email",
            "drname",
            "description",
        ]