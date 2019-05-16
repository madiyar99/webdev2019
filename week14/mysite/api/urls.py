from django.urls import path
from api import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('users/', views.UserList.as_view()),

    path('task_lists/', views.ListTaskLists.as_view()),
    path('task_lists/<int:pk>/', views.Tasks.as_view()),
    path('task_lists/<int:pk>/tasks/', views.Tasks.as_view())
]