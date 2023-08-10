from django.urls import path

from api import views

urlpatterns = [
    path("", views.TasksListAPIView.as_view()),
    path("new/", views.TasksCreateAPIView.as_view()),
    path("<uuid:pk>/", views.TasksRetrieveUpdateDestroyAPIView.as_view()),
]
