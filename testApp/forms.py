from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(label='email', required=True)
    name = forms.CharField(label='name', required=True)
    password = forms.CharField(label='password', widget=forms.Textarea, required=True)


