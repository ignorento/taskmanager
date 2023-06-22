from django.contrib import admin
from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path("tasks/", views.tasks_view, name="tasks"),
    path("create/", views.create_task_view, name='create'),
    path("<uuid:uuid>/", views.task_detail_view, name='detail'),
    path("<uuid:uuid>/update/", views.task_update_view, name='update'),
    path("<uuid:uuid>/delete/", views.task_delete_view, name='delete'),

]
