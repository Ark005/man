from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['title', 'cover','name', 'email', 'job_title', 'bio']


    

