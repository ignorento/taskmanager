from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from tasks.form import TaskCreateForm, TaskUpdateAssigneeForm
from tasks.models import TaskModel

class ListTasksView(ListView):
    model = TaskModel

class AboutPageView(TemplateView):
    template_name = "tasks/about.html"

class TaskDetailView(DetailView):
    model = TaskModel

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = TaskModel
    form_class = TaskCreateForm
    login_url = "/sign-up/"
    success_url = "/"
    extra_context = {"action": "Create"}

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskModel
    login_url = "/sign-up/"
    success_url = "/"
    extra_context = {"action": "Update"}

    def get_form_class(self):
        task = self.get_object()
        if task.reporter == self.request.user:
            return TaskCreateForm
        else:
            return TaskUpdateAssigneeForm

    def get_object(self, queryset=None):
        task = super().get_object(queryset=queryset)
        if not (task.reporter == self.request.user or task.assignee == self.request.user):
            raise PermissionDenied
        return task

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskModel
    login_url = "/sign-up/"
    success_url = "/"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.reporter != self.request.user or self.object.status:
            return HttpResponseForbidden("You don't have permission to delete this task.")

        return super().get(request, *args, **kwargs)
