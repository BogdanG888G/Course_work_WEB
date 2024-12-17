# jojo_app/forms.py

from django import forms
from main_app.models import Stand

class StandForm(forms.ModelForm):
    class Meta:
        model = Stand
        fields = '__all__'
