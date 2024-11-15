from django import forms

from habits.models import Habito

class HabitoForm(forms.ModelForm):
    class Meta:
        model = Habito
        fields = ['titulo'] 
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'border p-2 rounded-lg flex-grow mr-2'})
        }
