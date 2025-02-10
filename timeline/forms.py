from .models import ParentTask, ListItem
from django import forms

class CreateDailyForm(forms.ModelForm):
    class Meta:
        model=ParentTask
        fields = ['name']
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control ' ,'id':"floatingTitle"}), 
        }