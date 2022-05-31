"""chaeum_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from chaeum_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main_page, name = ''),
    path('Main',views.main_page, name = ''),
    path('login',views.login,name='login'),
    path('create_interior',views.create_interior,name='create_interior'),
    path('verify',views.verify,name='verify'),
    path('logout',views.logout,name='logout'),
    path('go_to_create',views.go_to_create_interior,name='go_to_create_interior'),
    path("mobile",views.send_to_mobile,name='mobile'),
    path("register",views.register,name='register'),
    path("create_account",views.create_account,name="create_account"),
    path("admit",views.admit,name='admit')
]
