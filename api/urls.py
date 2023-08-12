from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register("users", views.UserModelViewSet, "user")

urlpatterns = [
    path("", views.TasksListCreateAPIView.as_view()),
    path("auth/", obtain_auth_token, name="api-auth-token"),
    # path("new/", views.TasksCreateAPIView.as_view()),
    path("<uuid:pk>/", views.TasksRetrieveUpdateDestroyAPIView.as_view()),
    *router.urls
]
