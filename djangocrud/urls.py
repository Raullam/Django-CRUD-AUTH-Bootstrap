from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/pending/', views.pending_tasks, name='tasks_pending'),
    path('tasks/completed/', views.tasks_completed, name='tasks_completed'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('task/create/', views.create_task, name='create_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('signin/', views.signin, name='signin'),

]
