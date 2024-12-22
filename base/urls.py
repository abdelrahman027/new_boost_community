from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path("", views.login, name="login-view"),
    path('', views.login_user, name='login'),
    path("home/",views.index,name="home"),
    path("change-password/",auth_views.PasswordChangeView.as_view(),name="change-password"),

    path("profile/", views.profile, name="profile"),
    path("projects/", views.projects, name="projects"),
    path('projects/<int:id>',
         views.projects_detail, name='project-detail'),

    path("sales/", views.sales, name="sales"),

     path("learn-development/", views.learning_developers, name="learn-development"),
     
     path("repository/", views.repository, name="repo"),
     path("assesment-bank/", views.assesment_bank, name="assesment-bank"),
     path("simulation/", views.simulation, name="simulation"),

    path("clients/", views.clients, name="clients"),

    path('clients/<int:id>',
         views.clients_detail, name='clients-detail'),

    path("courses/", views.courses, name="courses"),   
    path("public-courses/", views.public_courses, name="public-courses"),
    path('courses/<int:id>',
         views.courses_detail, name='courses-detail'),

#     path("tasks/", views.tasks, name="tasks"),
    path('tasks/', views.create_own_Task, name='tasks'),
     
     # path('create_t/', views.task_create_view, name='create_t'),
    path('tasks/delete/<int:id>', views.delete_task, name='delete_task'),


    path('tasks/update/<int:id>', views.update_Task, name='update-task'),
     path('tasks/assign', views.assign_tasks, name='assign-task'),
     path('operations/', views.operations, name='operations'),
     path('designers/', views.designers, name='designers'),
     path('designers/requests', views.designer_requests, name='design-requests'),
     path('designers/templates', views.portoflio, name='portfolio'),
     path('employees/', views.employees_list, name='employees'),
     path('employees/<int:id>', views.employees_detail, name='employees-detail'),

     path('chat/', views.chat_gpt, name='chat_gpt'),
     # path('chatbot/', views.make_view.as_view(),name="chatbot"),

     path('logout/', views.logout_user, name='logout'),
     path('care/', views.care, name='care'),
     path('all_tasks/', views.AllTasks, name='all_tasks'),
     path('all_notifications/', views.all_Notifications, name='all_notifications'),
     path('mark-notifications-read/', views.mark_notifications_read, name='mark-notifications-read'),
     path('invoices/', views.invoices, name='invoices'),
     path('contracts/', views.contracts, name='contracts'),

]
