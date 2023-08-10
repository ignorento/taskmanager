from requests import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from tasks.models import TaskModel
from tasks.serializers import TaskSerializer, TaskListSerializer


class TasksListAPIView(ListCreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskListSerializer

class TasksCreateAPIView(ListCreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer

class TasksRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
