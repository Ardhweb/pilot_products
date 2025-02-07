from .models import DailyParent, AnchorCheckPoint, ListItem
from django import forms

class CreateDailyForm(forms.ModelForm):
    class Meta:
        model=DailyParent
        fields = ['name']
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control ' ,'id':"floatingTitle"}),
           
        }