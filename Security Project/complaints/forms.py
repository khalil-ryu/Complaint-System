from django import forms
from .models import Complaint
from cryptography.fernet import Fernet

class ComplaintForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Complaint
        fields = ['title', 'description']

