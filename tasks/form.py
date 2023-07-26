from django import forms
from django.contrib.auth.models import User

from .models import TaskModel
from users.models import UserModel

class TaskCreateForm(forms.Form):
    title = forms.CharField(max_length=64)
    description = forms.CharField(widget=forms.Textarea)
    # status = forms.BooleanField(required=False, initial=False)
    assignee = forms.ModelChoiceField(queryset=UserModel.objects.all(), empty_label=None)

class TaskUpdateAssigneeForm(TaskCreateForm):
    assignee = forms.ModelChoiceField(queryset=UserModel.objects.all(), empty_label=None, widget=forms.HiddenInput)
