from django import forms
from django.forms import fields
from .models import ToDoItem

class ToDoForm(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = '__all__'
