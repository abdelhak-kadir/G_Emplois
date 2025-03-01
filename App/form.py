from django import forms
from .models import EmploiDuTemps

class EmploiDuTempsForm(forms.ModelForm):
    class Meta:
        model = EmploiDuTemps
        fields = '__all__'
