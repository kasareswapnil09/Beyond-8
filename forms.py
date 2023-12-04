from django import forms
from .models import Nurse, Shift

class ScheduleForm(forms.Form):
    nurse = forms.ModelChoiceField(queryset=Nurse.objects.all())
    shift = forms.ModelChoiceField(queryset=Shift.objects.all())
    day = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
