from django.urls import path
from todo_app import views

urlpatterns = [
    path('', views.index,name='todos index'),
    path('create/', views.create, name='create_todo'),
    path('update/<int:pk>/', views.update, name='update_todo'),
    path('delete/<int:pk>/', views.delete, name='delete_todo'),
    path('todos/',views.todos_all,name='all_todos')

]
