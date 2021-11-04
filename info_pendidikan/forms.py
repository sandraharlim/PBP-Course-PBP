from django import forms
from django.forms import fields
from .models import InfoPendidikan

class infoForm(forms.ModelForm):
    class Meta:
        model = InfoPendidikan
        fields = '__all__'