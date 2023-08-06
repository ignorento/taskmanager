from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path("sign-up/", views.SignUpRegistrationView.as_view(), name='sign_up'),
    path("sign-in/", views.SignInLoginView.as_view(), name='sign_in'),
    path("logout/", views.UserLogoutView.as_view(), name='logout'),

]