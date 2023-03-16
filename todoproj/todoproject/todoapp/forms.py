from . models import Task
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields= ['name','priority','date'] #add all the fields/columns that need to be edited