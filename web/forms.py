from django import forms
from .models import ContactForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'message']
    

