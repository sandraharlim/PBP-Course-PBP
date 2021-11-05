from django import forms
from .models import Event

class DateInput(forms.DateInput):
    input_type = 'date'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            'Time':DateInput(attrs={'class': 'form-control'}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter event name'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Description of the event'}),
        }
