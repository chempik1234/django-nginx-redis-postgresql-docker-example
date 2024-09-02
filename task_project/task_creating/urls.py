from django.urls import path

from . import views

app_name = "task_creating"

urlpatterns = [
    path('test/', views.test_view)
]
