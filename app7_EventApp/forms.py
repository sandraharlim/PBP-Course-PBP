from django import forms
from .models import Event
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class EventForm(forms.ModelForm): 
    
    class Meta:
        model = Event
        fields = ('Name', 'Time', 'Description')
        widgets = {
            'Time':DateInput(attrs={'class': 'form-control'}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter event name'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Description of the event'}),
        }
        def form_valid(self, form):
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
