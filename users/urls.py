
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path("sign-up/", views.sign_up_view, name='sign_up'),
    path("sign-in/", views.sign_in_view, name='sign_in'),
    path("logout/", views.logout_view, name='logout'),

]