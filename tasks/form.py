from django import forms
from .models import TaskModel

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'assignee']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class TaskUpdateAssigneeForm(TaskCreateForm):
    class Meta(TaskCreateForm.Meta):
        fields = ['title', 'description']
