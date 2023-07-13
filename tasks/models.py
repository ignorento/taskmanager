from django.db import models
from django.contrib.auth import get_user_model
import uuid

UserModel = get_user_model()

class TaskModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=64)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    reporter = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name='reported_tasks')
    assignee = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name='assigned_tasks')

    def __str__(self) -> str:
        return self.title
