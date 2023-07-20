from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.
def sign_up_view(request: HttpRequest) -> HttpResponse:
    """
    User registration
    """
    return HttpResponse("Registration here")

def sign_in_view(request: HttpRequest) -> HttpResponse:
    """
    User login
    """
    return HttpResponse("Login here")

def logout_view(request: HttpRequest) -> HttpResponse:
    """
    User logout
    """
    return HttpResponse("Logout here")
