"""
URL configuration for projectname project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from toDo import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'), 
    path('register/', views.register_view, name='register'),  # URL for user registration
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_task, name='add_task'),  # URL for adding a task
    path('tasks/', views.task_list, name='task_list'),  # URL for viewing tasks
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # URL for editing a task
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle_task_status/<int:task_id>/', views.toggle_task_status, name='toggle_task_status'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('search/', views.search_task, name='search_task'),
]
