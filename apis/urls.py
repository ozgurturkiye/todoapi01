from django.urls import path

from . import views

urlpatterns = [
    path("todos/", views.todo_list, name="todo-list"),
    path("todos/<int:pk>/", views.todo_detail, name="todo-detail"),
    path("todos/add/", views.todo_add, name="todo-add"),
    path("todos/<int:pk>/change/", views.todo_change, name="todo-change"),
    path("todos/<int:pk>/delete/", views.todo_delete, name="todo-delete"),
]
