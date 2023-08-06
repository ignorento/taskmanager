from django.contrib import admin
from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path("", views.ListTasksView.as_view(), name="tasks"),
    path("create/", views.TaskCreateView.as_view(), name='create'),
    path("<uuid:pk>/", views.TaskDetailView.as_view(), name='detail'),
    path("<uuid:pk>/update/", views.TaskUpdateView.as_view(), name='update'),
    path("<uuid:pk>/delete/", views.TaskDeleteView.as_view(), name='delete'),
]
