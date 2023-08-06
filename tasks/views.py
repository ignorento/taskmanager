from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

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

    def get_object(self, queryset=None):
        task = super().get_object(queryset=queryset)
        if task.reporter == self.request.user:
            self.form_class = TaskCreateForm
        elif task.assignee == self.request.user:
            self.form_class = TaskUpdateAssigneeForm
        else:
            raise PermissionDenied
        return task

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskModel
    login_url = "/sign-up/"
    success_url = "/"
