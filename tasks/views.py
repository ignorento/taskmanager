from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User

from tasks.form import TaskCreateForm, TaskUpdateAssigneeForm
from tasks.models import TaskModel

from django.shortcuts import get_object_or_404, render, redirect


def tasks_view(request: HttpRequest) -> HttpResponse:
    """
    Homepage
    Tasks list view
    """
    tasks = TaskModel.objects.all()
    return render(request, "tasks/all_tasks.html", {'tasks': tasks})


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
    return render(request, 'tasks/detail_task.html', {'task': task})


@login_required
@require_http_methods(["GET", "POST"])
def create_task_view(request: HttpRequest) -> HttpResponse:
    """
    Create new task
    """
    if request.method == "POST":
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            status = False
            reporter = request.user
            assignee = form.cleaned_data['assignee']

            task = TaskModel.objects.create(
                title=title,
                description=description,
                status=status,
                reporter=reporter,
                assignee=assignee,
            )

            return redirect("/")
    # else:
    #     initial_data = {}
    #     if request.user.is_authenticated:
    #         initial_data['reporter'] = request.user.username
    #     form = TaskCreateForm(initial=initial_data)
    form = TaskCreateForm()

    return render(request, 'tasks/create_task.html', {'form': form})

@login_required
@require_http_methods(["GET", "POST"])
def task_update_view(request: HttpRequest, uuid) -> HttpResponse:
    """
    Update task
    """
    if request.method == "POST":
        task = get_object_or_404(TaskModel, id=uuid)
        if task.reporter == request.user:
            form = TaskCreateForm(request.POST)
            if form.is_valid():
                task.title = form.cleaned_data['title']
                task.description = form.cleaned_data['description']
                task.assignee = form.cleaned_data['assignee']
                task.save()

                return redirect('tasks:detail', uuid=uuid)

        if task.assignee == request.user:
            form = TaskUpdateAssigneeForm(request.POST)
            if form.is_valid():
                task.title = form.cleaned_data['title']
                task.description = form.cleaned_data['description']
                task.save()

                return redirect('tasks:detail', uuid=uuid)

    task = get_object_or_404(TaskModel, id=uuid)
    if task.reporter == request.user:
        form = TaskCreateForm(initial={
            'title': task.title,
            'description': task.description,
            'assignee': task.assignee,
        })
    if task.assignee == request.user:
        form = TaskUpdateAssigneeForm(initial={
            'title': task.title,
            'description': task.description,
            'assignee': task.assignee,
        })
    return render(request, 'tasks/update_task.html', {'form': form})

def task_delete_view(request: HttpRequest, uuid: str) -> HttpResponse:
    """
    Delete task
    """
    task = TaskModel.objects.get(id=uuid)
    task.delete()
    return redirect('/')

