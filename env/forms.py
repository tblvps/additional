# myapp/forms.py
from django import forms
from .models import TextFileUpload

class TextFileUploadForm(forms.ModelForm):
    class Meta:
        model = TextFileUpload
        fields = ['title', 'file']
