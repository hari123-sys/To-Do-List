from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='home'),
    path("create-an-activity/",views.todo_form,name='todoform'),
    path("todo/<str:title>/",views.viewData,name='viewData'),
    path("<int:id>/",views.delete_todo,name='delete'),
    path("edit<int:id>/",views.editTodo,name='edit'),
    path('done/<int:id>/',views.done,name='done'),
    path('completedTasks',views.completedTasks,name='completed'),
]