from django.forms import ModelForm
from django import forms

from app.models import TODO
class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title' , 'status' , 'description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control mb-5'})
        }