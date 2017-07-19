from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    phoneNumber = forms.CharField(required=True, label='Phone Number')
    address = forms.CharField(required=True, label='Address')
    city = forms.CharField(required=True, label='City')
    zipCode = forms.CharField(required=True, max_length=5, label='Zip Code')
