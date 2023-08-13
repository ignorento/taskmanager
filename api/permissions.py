from rest_framework.permissions import BasePermission
from tasks.models import TaskModel

class TaskReporterPermission(BasePermission):
    def has_object_permission(self, request, view, obj: TaskModel) -> bool:
        return obj.reporter == request.user

class TaskReporterOrAssigneePermission(BasePermission):
    def has_object_permission(self, request, view, obj: TaskModel) -> bool:
        return obj.reporter == request.user or obj.assignee == request.user
