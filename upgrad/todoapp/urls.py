from django.urls import path
from . import views
urlpatterns = [
    path('', views.TODOView.as_view(), name='home'),
    path('Complete/<todo_id>/', views.CompleteTodo, name = 'complete'),
    path('delete/', views.DeleteTodo, name = 'delete'),
    path('create/', views.TODOCreateView.as_view(), name ='article_create'),
    path('article/<int:pk>/edit/', views.TODOUpdateView.as_view(), name='article_edit'),
    path('article/<int:pk>/delete/', views.TODODeleteView.as_view(), name='article_delete'),
]
