from django import forms
from .models import ContactForm


class TextInputWidget(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'type': 'text'}
        super().__init__(*args, **kwargs)

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name','customer_email','message']
        widgets = {
            'customer_email': TextInputWidget(), 
        }
    

