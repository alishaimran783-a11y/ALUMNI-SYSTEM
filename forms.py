from django import forms
from .models import Alumni

class AlumniRegistrationForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['full_name', 'email', 'graduation_year', 
                  'course', 'phone', 'current_job']