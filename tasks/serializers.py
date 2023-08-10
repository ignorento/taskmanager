from rest_framework import serializers

from tasks.models import TaskModel
from users.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskModel
        fields = '__all__'

class TaskListSerializer(TaskSerializer):
    reporter = UserSerializer()
    assignee = UserSerializer()


