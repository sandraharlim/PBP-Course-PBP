from django import forms
from .models import Matkul

class MatkulForm(forms.ModelForm):
    class Meta:
        model = Matkul
        fields = ['name', 'day', 'start_time', 'end_time']