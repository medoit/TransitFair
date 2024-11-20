from django import forms
from .models import Citizen

class CitizenForm(forms.ModelForm):
    class Meta:
        model = Citizen
        fields = ['last_name', 'first_name', 'middle_name']  # Поля модели
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),  # HTML5-календарь
        }
