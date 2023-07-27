from django import forms
from App.models import *

class Topics(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
class Pages(forms.ModelForm):
    class Meta:
        model=Page
        fields=['name','url']
class Records(forms.ModelForm):
    class Meta:
        model=Record
        fields=['date','author']