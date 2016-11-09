from django import forms


class NameForm(forms.Form):
    location = forms.CharField(
        label="Location",
        max_length=128,
        required=False
    )
    lat = forms.CharField(label="Latitude", max_length=20, required=False)
    lng = forms.CharField(label="Longitude", max_length=20, required=False)

    def send_email(self):
        pass
