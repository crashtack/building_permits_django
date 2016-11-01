from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    location = forms.CharField(label="Location", max_length=128, required=False)
    lat = forms.CharField(label="Latitude", max_length=20, required=False)
    lng = forms.CharField(label="Longitude", max_length=20, required=False)

    def send_email(self):
        pass
