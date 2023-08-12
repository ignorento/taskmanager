from rest_framework import serializers

from tasks.models import TaskModel
from users.serializers import UserSerializer

class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskModel
        # fields = '__all__'
        exclude = ('reporter',)

class TaskListSerializer(serializers.ModelSerializer):
    reporter = UserSerializer()
    assignee = UserSerializer()

    class Meta:
        model = TaskModel
        fields = '__all__'

class TaskRetrieveUpdateDestroySerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskModel
        fields = '__all__'
        read_only_fields = ('reporter',)

class TaskRUDAssigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'
        read_only_fields = ('reporter', 'assignee',)
