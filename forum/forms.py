from django import forms
from .models import InfoPandemi, TipsKesehatan, CurahanHati

class AddInfoPandemi(forms.ModelForm):
    class Meta:
        model = InfoPandemi
        fields = '__all__'
        widgets = {
            'nama':forms.TextInput(attrs={'class':'form-control'}),
            'pekerjaan':forms.TextInput(attrs={'class':'form-control'}),
            'konten':forms.Textarea(attrs={'class':'form-control'}),
        }

class AddTipsKesehatan(forms.ModelForm):
    class Meta:
        model = TipsKesehatan
        fields = '__all__'
        widgets = {
            'nama':forms.TextInput(attrs={'class':'form-control'}),
            'pekerjaan':forms.TextInput(attrs={'class':'form-control'}),
            'konten':forms.Textarea(attrs={'class':'form-control'}),
        }

class AddCurahanHati(forms.ModelForm):
    class Meta:
        model = CurahanHati
        fields = '__all__'
        widgets = {
            'nama':forms.TextInput(attrs={'class':'form-control'}),
            'pekerjaan':forms.TextInput(attrs={'class':'form-control'}),
            'konten':forms.Textarea(attrs={'class':'form-control'}),
        }