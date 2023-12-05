from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import JOB_POSITIONS, GRADES, UserProfile

class SignUpForm(UserCreationForm):
    is_responsible = forms.BooleanField(
        label='Are you a responsible user?',
        required=False,
        initial=False,
        widget=forms.HiddenInput(),  # Use HiddenInput widget to hide the field in the form
    )

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=20)
    job_position = forms.ChoiceField(choices=JOB_POSITIONS)
    grade = forms.ChoiceField(choices=GRADES)

class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'job_position', 'grade', 'is_responsible','password1', 'password2', )
