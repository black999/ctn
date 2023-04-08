from django import forms
from obieg.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', 'zuzyto_cel', 'rodzaj_dokumentu', 'data_dok' )
        labels = {
            'description': 'Opis faktury',
        }
        widgets = {
            'description': forms.TextInput(attrs={'required': 'required', 'class': 'form-control'}),
            'document': forms.FileInput(attrs={'class':'form-control'}),
            'data_dok': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'zuzyto_cel': forms.Select(attrs={'class': 'form-control'}),
            'rodzaj_dokumentu': forms.Select(attrs={'class': 'form-control'}),
        }