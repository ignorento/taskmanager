from django.http.response import HttpResponse
from django.http.request import HttpRequest
from tasks.models import TaskModel

from django.shortcuts import get_object_or_404


def tasks_view(request: HttpRequest) -> HttpResponse:
    """
    Homepage
    Tasks list view
    """
    tasks = TaskModel.objects.all()
    return HttpResponse(tasks)


def about_page_view(request: HttpRequest) -> HttpResponse:
    """
    About
    """
    return HttpResponse("About application page")

def task_detail_view(request: HttpRequest, uuid: str) -> HttpResponse:
    """
    Show detail task
    """
    task = get_object_or_404(TaskModel, id=uuid)
    return HttpResponse(task)


def create_task_view(request: HttpRequest, args) -> HttpResponse:
    """
    Create new task
    """
    return HttpResponse("New task successfully created!")

def task_update_view(request: HttpRequest, uuid) -> HttpResponse:
    """
    Update task
    """
    return HttpResponse(f"Task successfully update: {uuid}")

def task_delete_view(request: HttpRequest, uuid: str) -> HttpResponse:
    """
    Delete task
    """
    return HttpResponse(f"Task delete: {uuid}")

