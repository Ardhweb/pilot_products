from django import forms

from aiapp.models import UploadAnalyzedFile
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

class UploadeFileForm(forms.ModelForm):
    
    class Meta:
        model = UploadAnalyzedFile
        fields = ['file']
        widgets ={
                
                'file':forms.FileInput(attrs={'id':"fileInput" ,

      'style':"display: block; width: 100%; padding: 0.5rem; border: 1px solid #d1d5db; border-radius: 0.375rem; background-color: #ffffff; color: #111827; font-size: 1rem;"}),
               
            }

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file:
            raise ValidationError("No file uploaded.")
        allowed_extensions = ['pdf', 'docx', 'txt']
        ext = file.name.split('.')[-1].lower()
        if ext not in allowed_extensions:
            raise ValidationError(f"Unsupported file extension: .{ext}. Allowed: {', '.join(allowed_extensions)}")
        allowed_mime_types = [
            'application/pdf',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'text/plain'
        ]
        if file.content_type not in allowed_mime_types:
            raise ValidationError("Unsupported file type.")

        # ✅ Optional: Check file size
        max_size_mb = 5
        if file.size > max_size_mb * 1024 * 1024:
            raise ValidationError(f"File size exceeds {max_size_mb}MB.")

        return file