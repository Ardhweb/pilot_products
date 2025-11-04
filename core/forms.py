from core.models import LetterDesign
from django import forms 

class BlankDesignForm(forms.ModelForm):
    class Meta:
        model = LetterDesign
        fields = ['state_data']
