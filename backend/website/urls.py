"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from task.views import add_task, get_tasks, accept_task, get_my_tasks, get_my_accepted_tasks
from user.views import create_user
from raiting.views import get_user_raiting, post_user_raiting
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),

    #get user token, requires username and password
    path('api-token-auth/', obtain_auth_token),

    #task specific api
    path('task_c/', add_task),
    path('tasks/', get_tasks),
    path('my_tasks/', get_my_tasks),
    path('accepted_tasks/', get_my_accepted_tasks),
    path('task_a/', accept_task),

    #raiting api
    path('raiting/', get_user_raiting),
    path('raiting_g/', post_user_raiting),

    #create user
    path('user_c/', create_user),
]
