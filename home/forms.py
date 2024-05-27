# forms.py
from django import forms
from .models import Person , Attendance ,Student

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['user', 'attendance']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']


