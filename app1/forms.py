# from typing import Tuple
from django import forms
from .models import Matkul

TEXT_CHOICES =(
    ("1", "Monday"),
    ("2", "Tuesday"),
    ("3", "Wednesday"),
    ("4", "Thursday"),
    ("5", "Friday"),
)

class MatkulForm(forms.ModelForm):
    class Meta:
        model = Matkul
        fields = ['name', 'day', 'start_time', 'end_time']
        # fields = "__all__"
        # widgets={
        #     'name':forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
        #     'day':forms.RadioSelect(choices=TEXT_CHOICES, attrs={'class':'form-control', 'id':'dayid'}),
        #     'start_time':forms.TimeInput(attrs={'class':'form-control', 'id':'starttimeid'}),
        #     'end_time':forms.TimeInput(attrs={'class':'form-control', 'id':'endtimeid'}),
        # }
    input_name = {
        'type' : 'text',
        'placeholder' : 'Masukan nama matkul'
    }
    input_start_time = {
        'type' : 'time',
    }
    input_end_time = {
        'type' : 'time',
    }
    name = forms.CharField(label='Name: ', required=True, 
            widget=forms.TextInput(attrs=input_name))
    day = forms.ChoiceField(choices=TEXT_CHOICES)
    start_time = forms.TimeField(label='Start Time: ', required=True, 
            widget=forms.TimeInput(attrs=input_start_time))
    end_time = forms.TimeField(label='Ended Time: ', required=True, 
            widget=forms.TimeInput(attrs=input_end_time))