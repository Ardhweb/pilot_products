from django import forms
from .models import CoverLetter

class CoverLetterForm(forms.ModelForm):

    class Meta:
        fields = ['title','contents']
        model = CoverLetter
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control ', "id":"title-text"}),
            'contents':forms.Textarea(attrs={'class':'form-control ', 'id':"prompt-content-response" , 'placeholder':'Dear Hiring Manager,I am writing to express my interest in the Front-End Developer position at Company Name, as advertised. With 10 years of experience in designing and'}),
            }