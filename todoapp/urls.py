from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('login', views.login_page, name='login'),
    path('register', views.register_page, name='register'),
    path('logout', views.logout_page, name='logout'),
    path('taskvisible', views.taskvisible, name='taskvisible'),
    path('createtask',views.createtask,name='createtask'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('taskvieweach/<int:pk>',views.viewtask,name='taskvieweach'),
    path('updatetask/<int:pk>',views.updatetask,name='updatetask'),
    path('privarcy', views.privacy, name='privacy'),
    path('terms_and_policy',views.terms,name='term_and_privacy'),
]
