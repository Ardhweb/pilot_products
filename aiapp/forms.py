from django import forms

from aiapp.models import UploadAnalyzedFile

class UploadeFileForm(forms.Form):
    
    class Meta:
        model = UploadAnalyzedFile()
        fields = '__all__'