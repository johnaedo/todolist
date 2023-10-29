from django import forms
from thelist.models import Tasks

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['descr']

class ListForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
