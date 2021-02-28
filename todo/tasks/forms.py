from django import forms
from .models import Task

class Create_task(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content','date_start','date_end','check_done']
        exclude = ['user']