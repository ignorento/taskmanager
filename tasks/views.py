from django.http.response import HttpResponse
from django.http.request import HttpRequest
from tasks.models import TaskModel

from django.shortcuts import render


def query_for_list(query) -> list:
    query_list = []
    for i in query:
        query_list.append(f"Title: {i.title}, "
                          f"Description: {i.description},"
                          f"Status: {i.status}, "
                          f"Created at: {i.created_at}, "
                          f"Updated at: {i.created_at}, "
                          f"Reporter: {i.reporter}, "
                          f"Assignee: {i.assignee}. ")
    return query_list


def tasks_view(request: HttpRequest) -> HttpResponse:
    """
    Homepage
    Tasks list view
    """
    tasks = TaskModel.objects.all()
    tasks_list = query_for_list(tasks)
    return HttpResponse(tasks_list)


def about_page_view(request: HttpRequest) -> HttpResponse:
    """
    About
    """
    return HttpResponse("About application page")

def task_detail_view(request: HttpRequest, uuid: str) -> HttpResponse:
    """
    Show detail task
    """
    task = TaskModel.objects.filter(id=uuid)
    task_list = query_for_list(task)
    return HttpResponse(task_list)

def create_task_view(request: HttpRequest) -> HttpResponse:
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

