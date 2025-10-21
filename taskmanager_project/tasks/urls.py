from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),    
    path('sign/', views.sign, name='sign'),
    path('add/', views.add, name='add'),
    path('edit/', views.edit_task, name='edit'),
    path('completed_task/', views.completed_tasks, name='completed_tasks'),
    path('about/', views.about, name='about'), 
    path('all/', views.all, name='all'),
]
