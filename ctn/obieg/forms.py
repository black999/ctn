from django import forms
from obieg.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', 'zuzyto_cel', 'rodzaj_dokumentu' )
        labels = {
            'description': 'Opis faktury',
        }
        widgets = {
            'description': forms.TextInput(attrs={'required' : 'required'}),
        }