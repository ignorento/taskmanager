from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.views.generic import FormView

from .forms import UserRegistrationForm


class SignUpRegistrationView(FormView):
    template_name = "users/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:sign_in")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save_new_user()
        return super().form_valid(form)


class SignInLoginView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks:tasks')


class UserLogoutView(LoginRequiredMixin, LogoutView):

    def get_success_url(self):
        return reverse_lazy("tasks:tasks")
