"""ii URL Configuration

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
from django.conf.urls import url
from . import views

#app_name = 'ii'
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.index, name='index'),
    path('', views.user_login, name='user_login'),
    path('profile/', views.profile, name='profile'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('home/', views.home, name='home'),
    path('message/', views.message, name='message'),
    path('signup/', views.signup, name='signup'),
    path('thanks/', views.thanks, name='thanks'),
    path('studentlist/', views.student_list, name='studentlist' ),
    path('profile/<int:institute_id>/', views.single_student, name='single_student'),
   # path('images/', views.display_student_image, name = 'student_image'),
    
    #path('', include(('views.user_login', 'user_login'), namespace='ii'))
    #url(r'^login/$', views.user_login, name='user_login')
]
