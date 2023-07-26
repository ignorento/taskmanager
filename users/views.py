from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http.request import HttpRequest
from django.views.decorators.http import require_http_methods

from .forms import UserRegistrationForm, UserLoginForm


@require_http_methods(["GET", "POST"])
def sign_up_view(request: HttpRequest) -> HttpResponse:
    """
    User registration
    """
    if request.user.is_authenticated:

        return redirect('/')

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save_new_user()

            return HttpResponseRedirect("/sign-in/")
    else:
        form = UserRegistrationForm()

    return render(request, "users/register.html", {"form": form})


@require_http_methods(["GET", "POST"])
def sign_in_view(request: HttpRequest) -> HttpResponse:
    """
    User login
    """
    if request.user.is_authenticated:

        return redirect('/')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("/")
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form})


def logout_view(request: HttpRequest) -> HttpResponse:
    """
    User logout
    """
    logout(request)
    return redirect('/')
