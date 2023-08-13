from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.authtoken.models import Token

from .permissions import TaskReporterPermission, TaskReporterOrAssigneePermission

from tasks.models import TaskModel
from tasks.serializers import TaskCreateSerializer, TaskListSerializer, TaskRetrieveUpdateDestroySerializer, \
    TaskRUDAssigneeSerializer
from users.models import UserModel
from users.serializers import UserSerializer


class TasksListCreateAPIView(ListCreateAPIView):
    queryset = TaskModel.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return TaskListSerializer
        else:
            return TaskCreateSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        else:
            return [IsAuthenticated(), TaskReporterPermission()]

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)

# class TasksCreateAPIView(ListCreateAPIView):
#     queryset = TaskModel.objects.all()
#     serializer_class = TaskSerializer

class TasksRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()

    def get_serializer_class(self):
        instance = self.get_object()

        if self.request.method in ["PUT", "PATCH"]:
            if instance.reporter == self.request.user:
                return TaskRetrieveUpdateDestroySerializer
            elif instance.assignee == self.request.user:
                return TaskRUDAssigneeSerializer

        return TaskRetrieveUpdateDestroySerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        elif self.request.method in ["PUT", "PATCH"]:
            return [IsAuthenticated(), TaskReporterOrAssigneePermission()]
        elif self.request.method == "DELETE":
            return [IsAuthenticated(), TaskReporterPermission()]
        return [IsAuthenticated()]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status:
            return Response({"detail": "This task is completed."}, status=status.HTTP_400_BAD_REQUEST)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class UserModelViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #
    #     user = serializer.instance
    #
    #     # Удаляем существующий токен пользователя, если он есть
    #     Token.objects.filter(user=user).delete()
    #
    #     # Создаем и сохраняем новый токен для пользователя
    #     token = Token.objects.create(user=user)
    #
    #     # Возвращаем данные пользователя вместе с токеном в ответе
    #     user_data = serializer.data
    #     user_data['token'] = token.key
    #
    #     return Response(user_data, status=status.HTTP_201_CREATED)

