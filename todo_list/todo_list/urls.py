"""todo_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from webapp.views import index_view, create_view, delete_view, complete_task_view, edit_task_view, delete_all_done_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name="task_index"),
    path('create', create_view, name="task_create"),
    path('task/<int:task_pk>/delete', delete_view, name="task_delete"),
    path('task/<int:task_pk>/complate', complete_task_view, name="task_complete"),
    path('task/<int:task_pk>/edit', edit_task_view, name="task_edit"),
    path('delete', delete_all_done_view, name="delete_done")
]
