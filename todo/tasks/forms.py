from django import forms
from .models import Task
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget


class time_end1(forms.TimeInput):
    input_type = 'time'


class Create_task(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'date_start', 'date_end', 'time_end']
        exclude = ['user']
        widgets = {
            'date_end': forms.SelectDateWidget,
            'time_end': time_end1(),
        }